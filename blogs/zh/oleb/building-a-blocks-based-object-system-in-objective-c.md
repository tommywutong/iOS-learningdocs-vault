---
title: 在（Objective-）C 中构建基于 `block` 的对象系统
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/02/building-blocks-based-object-system-in-objective-c/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7a64a9e9465abded'
translated: true
---

> 原文：[Building a Blocks-Based Object System in (Objective-)C](https://oleb.net/blog/2013/02/building-blocks-based-object-system-in-objective-c/)　·　Ole Begemann

# 在（Objective-）C 中构建基于 `block` 的对象系统

我正在阅读著名的 MIT 教材《计算机程序的构造和解释》（[Structure and Interpretation of Computer Programs](http://mitpress.mit.edu/sicp/)）。你可能知道，这本书使用 Lisp 方言 [Scheme](https://en.wikipedia.org/wiki/Scheme_%28programming_language%29) 来教授编程。

书中大量篇幅集中在函数式编程（[functional programming](https://en.wikipedia.org/wiki/Functional_programming)）上，尽量避免使用状态（state）和可变数据（mutable data）。不过，在某个地方，我发现了一个与我们在 Objective-C 中实践的面向对象编程（object-oriented programming）的有趣类比。

# 基于函数的对象模型

在第 3 章中，作者介绍了一种程序组织策略，将大型系统视为一组不同的 _对象_（objects）的集合，这些对象的行为可能随时间变化（即它们拥有可变的 _状态_）。这听起来就像 Objective-C 中的对象。

Scheme 没有定义特殊的语法来定义对象，所以我很想知道作者在 Scheme 中是如何建模对象的。结果他们使用了函数。书中的例子是一个银行账户对象。银行账户在构造时获取初始余额，并响应两个消息：`withdraw` 和 `deposit`，用于修改余额。

在 Scheme 中，银行账户“对象”是这样定义的：

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

这段代码定义了一个名为 `(make-account balance)` 的函数，它接受账户的初始余额作为参数。函数体内又定义了三个函数：

1. `(withdraw amount)`，从总余额 `balance` 中减去参数中的金额，并返回新余额（如果账户余额不足以完成取款请求，则返回错误）。
2. `(deposit amount)`，将参数中的金额加到总余额 `balance` 上，并返回新余额。
3. `(dispatch m)` 函数，它检查其参数（_消息_）是否等于 `'withdraw'` 或 `'deposit'`，并返回相应的函数（如果参数不匹配则返回错误）。

关键在于，`make-account` 函数的返回结果并不是严格意义上的银行账户对象，而是 `dispatch` 函数本身。因此，通过调用 `make-account`，你会得到一个函数，然后你可以用一个 _消息_（一个符号或字符串，指定应由对象执行的命令）来调用它——在我们的例子中是 `'withdraw'` 或 `'deposit'`。根据其参数，`dispatch` 函数（即“银行账户对象”）会返回另一个函数，该函数代表消息指定的命令。

在 Scheme 代码中，`make-account` 的使用方式如下：

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

# 在（Objective-）C 中重建

我很想知道是否以及如何用 C/Objective-C 重建这个设计。我们可以使用 [`block`](https://en.wikipedia.org/wiki/Blocks_(C_language_extension)) 来模拟 Scheme 的函数，这些函数可以捕获状态，并作为参数和返回值传递。

由于 `block` 是在语言的 C 层面上定义的，因此完全不需要使用任何 Objective-C 特性。不过，我出于方便考虑，为了将不同的类型（`NSNumber` 和 `NSError`）封装在同一个返回类型 `id` 下，还是使用了 Objective-C。

我的（Objective-）C 解决方案如下（[从 GitHub 下载 Objective-C 代码](https://gist.github.com/ole/4755072)）：

```
BankAccount CreateBankAccount(double initialBalance)
{
    // 初始化
    NSCAssert(initialBalance >= 0.0, @"initialBalance must not be negative");
    double __block balance = initialBalance;

    // "方法定义"
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

    // 消息分发
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

C 函数 `CreateBankAccount()` 返回一个 `block`，该 `block` 充当消息分发器。用该“对象”能理解的消息（或选择器（selector），`"currentBalance"`、`"deposit"` 或 `"withdraw"`）调用这个 `block`，会返回另一个 `block`，该 `block` 代表与该选择器对应的相应方法。否则，分发 `block` 会返回一个 `NSError` 对象。

由于这些“方法” `block` 捕获并修改了定义在 `CreateBankAccount()` 函数中的变量 `balance`，因此它充当了银行账户“对象”的实例变量（instance variable）。

下面是如何使用这个对象：

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

这段代码看起来有点丑陋，因为我们需要根据参数的不同，将分发 `block` 的返回值转换为不同的 `block` 类型，但除此之外，它是一个可用的对象系统。很不错！

# 实际应用性

零。显然，这只是一个我喜欢的实验，在实践中没有任何用处。在其当前形式下，该对象系统不支持继承。此外，为每个“类”手动编写消息分发器正是我们不想做的事情。
