---
title: Building a Blocks-Based Object System in (Objective-)C
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/02/building-blocks-based-object-system-in-objective-c/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7a64a9e9465abded'
translated: false
---

> 原文：[Building a Blocks-Based Object System in (Objective-)C](https://oleb.net/blog/2013/02/building-blocks-based-object-system-in-objective-c/)　·　Ole Begemann

# Building a Blocks-Based Object System in (Objective-)C

I am currently reading the well-known MIT book [Structure and Interpretation of Computer Programs](http://mitpress.mit.edu/sicp/). As you probably know, the book uses the Lisp dialect [Scheme](https://en.wikipedia.org/wiki/Scheme_%28programming_language%29) to teach programming.

A large portion of the book concentrates on [functional programming](https://en.wikipedia.org/wiki/Functional_programming), avoiding state and mutable data wherever possible. At one point, though, I found an interesting analogy to object-oriented programming as we practice it in Objective-C.

# An Object Model Based On Functions

In chapter 3, the authors introduce an organizational strategy for a program that views a large system as a collection of distinct _objects_ whose behaviors may change over time (i.e., that have mutable _state_). This sounds just like objects in Objective-C.

Scheme does not define a special syntax to define objects, so I was curious how the authors modeled objects in Scheme. It turns out they use functions. The example in the book is an object for a bank account. The bank account gets initial balance upon construction and responds to two messages, _withdraw_ and _deposit_, used to modify the balance.

In Scheme, the bank account “object” is defined like this:

```
(define (make-account balance)
  (define (withdraw amount)
    (if (>= balance amount)
        (begin (set! balance (- balance amount))
               balance)
        "Insufficient funds"))

  (define (deposit amount)
    (set! balance (+ balance amount))
    balance)

  (define (dispatch m)
    (cond ((eq? m 'withdraw) withdraw)
          ((eq? m 'deposit) deposit)
          (else (error "Unknown request -- MAKE-ACCOUNT"
                       m))))

  dispatch)
```

This snippet defines a function named `(make-account balance)` that takes the account’s initial balance as an argument. The function body begins with three more function definitions:

1. `(withdraw amount)`, which subtracts the amount in its argument from the overall `balance` and returns the new balance (or an error if the account balance is insufficient to fulfill the withdraw request.
2. `(deposit amount)`, which adds the amount in its argument to the overall `balance` and returns the new balance.
3. A `(dispatch m)` function that checks whether its argument (the _message_) equals either `'withdraw'` or `'deposit'` and returns the corresponding function (or an error if the argument does not match either).

Crucially, the result of the `make-account` function is not some bank account object in the stricter sense but the `dispatch` function itself. So by invoking `make-account`, you get a function that you can then call with a _message_ (a symbol or string that specifies a command that should be executed by the object) – ‘withdraw’ or ‘deposit’ in our case. Depending on its argument, the `dispatch` function (i.e., the “bank account object”) returns another function which represents the command specified by the message.

In Scheme code, usage of `make-account` looks like this:

```
(define acc (make-account 100))

((acc 'withdraw) 50)
; 50
((acc 'withdraw) 60)
; "Insufficient funds"
((acc 'deposit) 40)
; 90
((acc 'withdraw) 60)
; 30
```

# Rebuilding it in (Objective-)C

I was curious if and how one could rebuild this design in C/Objective-C. We could use [blocks](https://en.wikipedia.org/wiki/Blocks_(C_language_extension)) to model Scheme’s functions that can capture state and be passed around as arguments and return variables.

Since blocks are defined on the C level of the language, there is no need to use any Objective-C features at all. Im am doing so anyway, though, mainly for convenience reasons of encapsulating different types (`NSNumber` and `NSError`) under the same return type `id`.

My solution in (Objective-)C is as follows ([Download the Objective-C code from GitHub](https://gist.github.com/ole/4755072)):

```
BankAccount CreateBankAccount(double initialBalance)
{
    // Initialization
    NSCAssert(initialBalance >= 0.0, @"initialBalance must not be negative");
    double __block balance = initialBalance;

    // "Method Definitions"
    CurrentBalanceMethod currentBalance = ^id{
        return @(balance);
    };

    DepositMethod deposit = ^id(double depositAmount)
    {
        NSCAssert(depositAmount > 0.0, @"depositAmount must be greater than zero");
        balance = balance + depositAmount;
        return @(balance);
    };

    WithdrawMethod withdraw = ^id(double withdrawAmount)
    {
        NSCAssert(withdrawAmount > 0.0, @"withdrawAmount must be greater than zero");
        BOOL hasSufficientBalance = (balance >= withdrawAmount);
        if (hasSufficientBalance) {
            balance = balance - withdrawAmount;
            return @(balance);
        } else {
            return [NSError errorWithDomain:@"BankAccountErrorDomain" code:2 userInfo:@{ NSLocalizedDescriptionKey : @"Insufficient balance" }];
        }
    };

    // Message Dispatch
    id bankAccountBlock = ^id(char *cmd)
    {
        if (strcmp(cmd, "currentBalance") == 0) {
            return currentBalance;
        } else if (strcmp(cmd, "deposit") == 0) {
            return deposit;
        } else if (strcmp(cmd, "withdraw") == 0) {
            return withdraw;
        } else {
            return [NSError errorWithDomain:@"BankAccountErrorDomain" code:1 userInfo:@{ NSLocalizedDescriptionKey : @"Unknown selector" }];
        }
    };

    return bankAccountBlock;
}
```

The C function `CreateBankAccount()` returns a block that acts as the message dispatcher. Calling this block with a message (or selector) the “object” understands (`"currentBalance"`, `"deposit"` or `"withdraw"`) returns another block that represents the respective method corresponding to the selector. Otherwise, the dispatch block returns an `NSError` object.

Since the “method” blocks capture and modify the variable `balance` defined in the `CreateBankAccount()` function, it acts as an instance variable of the bank account “object”.

Here’s how one would use this object:

```
BankAccount account = CreateBankAccount(100);

NSNumber *balance = ((CurrentBalanceMethod)account("currentBalance"))();
NSLog(@"Balance: %@", balance);
balance = ((DepositMethod)account("deposit"))(50);
NSLog(@"Depositing 50, new balance: %@", balance);
balance = ((WithdrawMethod)account("withdraw"))(30);
NSLog(@"Withdrawing 30, new balance: %@", balance);
balance = ((WithdrawMethod)account("withdraw"))(100);
NSLog(@"Withdrawing 100, new balance: %@", balance);
```

The code looks a little ugly because we need to cast the return values of our dispatcher block to different block types depending on their arguments, but other than that it is functional object system. Neat!

# Practical Applicability

Zero. Obviously, this is just an experiment I enjoyed with no usefulness in practice. In its current form, the object system does not support inheritance, for example. Also, writing a message dispatcher manually for each “class” is exactly what we do not want to do.
