---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/WebScript/ModernSyntax.html
archived_at: '2026-07-15T07:48:02.918192Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.mif.book.md)
[!Previous Section](ScriptedClasses.md)

## "Modern" WebScript Syntax

When you designate an action method in WebObjects Builder, it can emit code similar to this (if the appropriate preference is selected):

```
function submit() {
}
```

This is an instance of "modern" syntax, a variation of WebScript designed to appeal to programmers more familiar with such languages as Visual Basic and Java. The rules for transformming "classic" WebScript to "modern" WebScript can be illustrated by examples that map one to another.

#### Method Definition

Classic:

```
- submit {
  // <body>
}
```

Modern:

```
function submit() {
  // <body>
}
```

#### Method Invocation --- No Argument

Classic:

```
[self doIt];
```

Modern:

```
self.doIt();
```

#### Method Invocation --- One Argument

Classic:

```
[guests addObject:newGuest];
```

Modern:

```
guests.addObject(newGuest);
```

#### Method Invocation --- Two or More Arguments

Classic:

```
[guests insertObject:newGuest atIndex:anIndex];
```

Modern:

```
guests.insert(object := newGuest, atIndex := anIndex);
```

Note that in this last example that the left parenthesis can occur at any point before the first argument. You can even have no keyword on the left side of the first assignment. Thus the following two mappings would be valid as well:

```
guests.insertObjec(t := newGuest, atIndex := anIndex); // not recommended!
guests.insertObject(newGuest, atIndex := anIndex);
```

However, if the "modern" message is to map to an existing Objective-C method (which, of course, follows "classic" WebScript syntax), then the characters just inside the left parenthesis (that is, on the left side of the first assignment) are significant. When WebScript transforms "modern" to "classic" syntax internally, it capitalizes this character before concatentating the keywords of the selector. Thus the first example immediately above would change to "classic" syntax as:

```
[guests insertObjecT:newGuest atIndex:anIndex];
```

If you choose to use \x81modern\x86 WebScript, there is another important caveat to be aware of: You cannot have methods with variable arguments. So if you stick with straight \x81modern\x86 syntax, you cannot use \x81classic\x86 methods such as __logWithFormat:__ and __stringWithFormat:__. You can, however, mix \x81classic\x86 and \x81modern\x86 WebScript in the same script file.

By default WebObjects Builder emits "classic" WebScript syntax. If you want to work with "modern" syntax, choose the appropriate option in the Language display of Preferences.
