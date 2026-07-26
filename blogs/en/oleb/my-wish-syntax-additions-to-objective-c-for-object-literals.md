---
title: 'My Wish: Syntax Additions to Objective-C for Object Literals'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/12/syntax-additions-for-object-literals-to-objective-c/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:902eadbd59c09c74'
translated: false
---

> 原文：[My Wish: Syntax Additions to Objective-C for Object Literals](https://oleb.net/blog/2010/12/syntax-additions-for-object-literals-to-objective-c/)　·　Ole Begemann

# My Wish: Syntax Additions to Objective-C for Object Literals

I have [written](https://oleb.net/blog/2010/12/method-names-in-objective-c/) [before](https://oleb.net/blog/2010/03/if-you-want-to-learn-cocoa/) about the preference for clarity over brevity in the Objective-C/Cocoa world that leads to extraordinarily long method signatures. While I like the expressiveness of this approach, there are occasions where I feel the language could be more concise without giving up anything. Most of the time, this has to do with often-used objects like `NSNumber`, `NSArray`, and `NSDictionary`. I wish Objective-C included a syntax to quickly define object literals of these types as we can already do with strings.

Objective-C has understood the syntax `@"Some string"` to define a literal string object for a long time (not since the beginning, though: the `@"..."` was not part of the original implementation of Objective-C). So why not define a similar syntax for other object literals? Here are some I would love to see in a future version of the language:

| New syntax | Equivalent to |
|---|---|
| `@1` | `[NSNumber numberWithInteger:1]` |
| `@2.5f` | `[NSNumber numberWithFloat:2.5f]` |
| `@2.5` | `[NSNumber numberWithDouble:2.5]` |
| `@YES` | `[NSNumber numberWithBool:YES]` |
| `@[@"abc", @1, @2.5, @NO]` | `[NSArray arrayWithObjects:@"abc", [NSNumber numberWithInteger:1], [NSNumber numberWithDouble:2.5], [NSNumber numberWithBool:NO], nil]` |
| `@{ @"name": @"John Appleseed", @"age": @38 }` | `[NSDictionary dictionaryWithObjectsAndKeys: @"John Appleseed", @"name", [NSNumber numberWithInteger:38], @"age", nil]` |

As an example of how such syntax additions could influence the look of your code, consider the creation of a keyframe animation. Currently:

```
CAKeyframeAnimation *animation = [CAKeyframeAnimation animationWithKeyPath:@"alpha"];
animation.values   = [NSArray arrayWithObjects:
                      [NSNumber numberWithFloat:1.0f],
                      [NSNumber numberWithFloat:0.8f],
                      [NSNumber numberWithFloat:0.0f],
                      nil];
animation.keyTimes = [NSArray arrayWithObjects:
                      [NSNumber numberWithFloat:0.0f],
                      [NSNumber numberWithFloat:0.6f],
                      [NSNumber numberWithFloat:1.0f],
                      nil];
[self.view.layer addAnimation:animation forKey:@"alpha"];
```

With the new syntax, this could be written in a much clearer way in my opinion:

```
CAKeyframeAnimation *animation = [CAKeyframeAnimation animationWithKeyPath:@"alpha"];
animation.values   = @[@1.0f, @0.8f, @0.0f];
animation.keyTimes = @[@0.0f, @0.6f, @1.0f];
[self.view.layer addAnimation:animation forKey:@"alpha"];
```

**Update January 14, 2011:** Comments from readers:

Jens Ayton:

> allow the @ to be dropped inside compound literals, since you can’t put primitives there anyway. Also, allow keyword-like dictionary keys to be unquoted, as in JavaScript.

Bavarious points to a set of macros Mike Ash has created to simplify the making of collections: [MACollectionUtilities](https://github.com/mikeash/MACollectionUtilities). The syntax isn’t as nice, but they are easy to implement.

My coworkers Christian and Alexis suggest two more literals:

- for
- for

  with binary content (in hex)

---

**Update May 10, 2012:** Stig Brautaset pointed out to me that [he already wrote about this topic in 2008](http://skuggdev.wordpress.com/2008/08/25/objective-c-syntax-sugar-wish-list/) and made very similar suggestions. Thanks Stig, I didn’t know!
