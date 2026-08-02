---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/WebScript14.html
archived_at: '2026-07-18T01:20:35.667546Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](The%20WebScript%20Language.md) [!Previous Section](WebScript13.md)

## "Modern" WebScript Syntax

WebScript supports two syntax styles. The style that you've been reading about up until now is "classic" syntax, which is based on the syntax of Objective-C. If you're more familiar with languages such as Visual Basic or Java, you may be more comfortable with the alternate syntax style, called "modern" syntax.
The differences between classic and modern WebScript syntax are summarized below:

- Method Definition

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

- Method Definition With Arguments

Classic:

```
    - takeValuesFromRequest:(WORequest *)request
        inContext:(WOContext *)context {
    // <body>
}
```


Modern:

```
    //Note: no static typing allowed.
    function takeValues(fromRequest:= request inContext:=
context){
        // <body>
    }
```

- Method Invocation - No Argument

Classic:

```
    [self doIt];
```


Modern:

```
    self.doIt();
```

- Method Invocation - One Argument

Classic:

```
    [guests addObject:newGuest];
```


Modern:

```
    guests.addObject(newGuest);
```

- Method Invocation - Two or More Arguments

Classic:

```
    [guests insertObject:newGuest atIndex:anIndex];
```


Modern:

```
    guests.insert(object := newGuest, atIndex := anIndex);
```


Note that in this last example the left parenthesis should occur at a break between words when the modern message maps to an existing Objective-C method (which, of course, follows classic WebScript syntax). When WebScript transforms modern to classic syntax internally, it capitalizes this character before concatenating the keywords of the selector. Thus, any of the following is correct:

```
super.takeValuesFrom(request := request, inContext :=
context);
super.takeValues(fromRequest := request, inContext :=
context);
super.take(valuesFromRequest := request, inContext :=
context);
```


If you choose to use modern WebScript, there is another important caveat: You cannot have methods with variable-length argument lists. Thus, you cannot use methods such as __logWithFormat:__ and __stringWithFormat:__. You can, however, mix classic and modern WebScript in the same script file.

[!Table of Contents](The%20WebScript%20Language.md) [!Next Section](Advanced%20WebScript.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
