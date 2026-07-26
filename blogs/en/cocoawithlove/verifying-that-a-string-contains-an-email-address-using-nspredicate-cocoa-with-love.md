---
title: 'Verifying that a string contains an email address using NSPredicate | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/06/verifying-that-string-is-email-address.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:2c6a7f67e2b554b1'
translated: false
---

> 原文：[Verifying that a string contains an email address using NSPredicate | Cocoa with Love](https://www.cocoawithlove.com/2009/06/verifying-that-string-is-email-address.html)　·　Cocoa with Love (Matt Gallagher)

To celebrate the official release of iPhone OS 3.0 this week, I will show you how to verify that an NSString contains a syntactically valid email address using NSPredicate — a class that joins the iPhone SDK 3.0 as part of the Core Data additions. This code will work on Mac OS X too since, as with the rest of Core Data, NSPredicate has been part of Mac OS X since 10.4 (Tiger).

## Before I begin...

I gave an interview to Anthony Agius of [MacTalk.com.au](http://www.mactalk.com.au) this week. You can [download the MP3 from their website](http://www.mactalk.com.au/2009/06/23/mactalk-interviews-10-matt-gallagher-cocoa-with-love/). I'm hesitant to listen to my own voice but I think I talked about what it's like to be an independent Mac/iPhone developer in Melbourne, Australia.

## Back to predicates

In programming, a predicate is a condition that returns true or false if the object it processes has the properties that the predicate describes. The key difference between a predicate and a regular boolean expression is that a predicate only considers the properties of one object, where a boolean expression may consider multiple, unrelated objects.

Many programmers are familiar with predicates as used in SQL database queries. For example a query to extract the complete row from the "people" database table for every person named "John Smith" might look like this in SQL:

```objc
SELECT * FROM people WHERE firstname = 'John' AND lastname = 'Smith'
```

Everything after the "WHERE" is the predicate — it looks at properties of the row only and is either true (the row will be extracted) or false (the row will be ignored).

## Using NSPredicate to evaluate predicates

In Cocoa, `NSPredicate` works in much the same way as the "WHERE" clause of SQL. The main reason that `NSPredicate` is being brought to the iPhone is that `NSPredicate` fulfils the same role in Core Data that "WHERE" clauses fulfil in SQL — to allow the persistent store to fetch objects that satisfy specific criteria.

Imagine we had an `NSDictionary` created using the following method:

```objc
- (NSDictionary *)personRowWithFirstname:(NSString *)aFirstname
    lastname:(NSString *)aLastname
{
    return
        [NSDictionary dictionaryWithObjectsAndKeys:
            aFirstname, @"firstname",
            aLastname, @"lastname",
        nil];
}
```

we could test if a given row created by this method matched the predicate "`firstname = 'John' AND lastname = 'Smith'`" with the following:

```objc
// given an NSDictionary created used the above method named "row"...
NSPredicate *johnSmithPredicate =
    [NSPredicate predicateWithFormat:@"firstname = 'John' AND lastname = 'Smith'"];
BOOL rowMatchesPredicate = [johnSmithPredicate evaluateWithObject:row];
```

The [string format used to construct an `NSPredicate` in Cocoa](http://developer.apple.com/DOCUMENTATION/Cocoa/Conceptual/Predicates/Articles/pSyntax.html#//apple_ref/doc/uid/TP40001795) is very similar to the syntax of the "WHERE" clause in SQL. You can also construct this `NSPredicate` in code by building it from two `NSComparisonPredicate`s and an `NSCompoundPredicate`.

A more common use of `NSPredicate` is filtering — extracting rows that match an `NSPredicate` from a larger collection:

```objc
// given an NSArray of rows named "rows" and the above "johnSmithPredicate"...
NSArray *rowsMatchingPredicate = [rows filteredArrayUsingPredicate:johnSmithPredicate];
```

This is then more like an SQL query where we have selected matching rows from the larger table of data.

> **Note:**`NSPredicate` handles filtering only. If you'd like to replicate SQL's "ORDER BY" clause, you can apply `NSSortDescriptor` as a separate step.

## Verifying an email address

The "LIKE" comparison operator in `NSPredicate` (`NSLikePredicateOperatorType`) is commonly used as a convenient means of testing if an `NSString` matches a Regular Expression. It's advantage over full libraries with greater options and replacement capability is that it is already in Cocoa — no libraries, no linkage, no hassle.

To test if an `NSString` matches a regular expression, we can use the following code:

```objc
NSPredicate *regExPredicate =
    [NSPredicate predicateWithFormat:@"SELF MATCHES %@", regularExpressionString];
BOOL myStringMatchesRegEx = [regExPredicate evaluateWithObject:myString];
```

The only question that remains is: what is a regular expression that can be used to verify that an `NSString` contains a syntactically valid email address?

```objc
NSString *emailRegEx =
    @"(?:[a-z0-9!#$%\\&'*+/=?\\^_`{|}~-]+(?:\\.[a-z0-9!#$%\\&'*+/=?\\^_`{|}"
    @"~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\"
    @"x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-"
    @"z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5"
    @"]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-"
    @"9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21"
    @"-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])";
```

This regular expression is adapted from a version at [regular-expressions.info](http://www.regular-expressions.info/email.html) and is a complete verification of RFC 2822.

This adaptation involved escaping all backslashes with another backslash (otherwise the `NSString` will try to interpret them before they are used in the Regular Expression) and escaping the ampersands (&) so it isn't interpreted as a Unicode escape sequence and caret (^) characters because — actually I have no idea why except that the expression wouldn't parse without it.

The linked [regular-expressions.info](http://www.regular-expressions.info/email.html) page recommends using slightly different regular expressions that force the top-level domain to be a country code or a known top-level domain. With the number of top-level domains due to increase in the near future, I'm not sure this is a good constraint to impose — since this check isn't intended to verify that the provided domain name is valid.

Since this regular expression `NSString` is so long, I've split it over 7 lines. This is an underused feature in Standard C languages — if you split a string into pieces but put nothing except whitespace between the pieces, the compiler will treat it as one continuous string. You don't need to write an extremely long string on a single long line.

## Conclusion

Just a few lines of code this week but I thought it would be good to draw attention to one of the minor additions making its way to the iPhone in SDK 3.0. I use `NSPredicate` all the time on Mac OS to perform searches, extract subarrays and perform quick Regular Expression tests. Without it, the only alternatives on the iPhone were methodical array iterations and manual comparisons in code.
