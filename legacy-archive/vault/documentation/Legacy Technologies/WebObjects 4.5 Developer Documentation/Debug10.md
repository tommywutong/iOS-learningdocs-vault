---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Debug10.html
archived_at: '2026-07-15T08:05:10.781022Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Debugging%20a%20WebObjects%20Application.md) [!Previous Section](Debug9.md)

## Debugging Dynamic Elements and Reusable Components

If a dynamic element's or resuable component's bindings are not working like you expect them to, or you just want more insight into how non-synchronized components work, you can enable debugging for that element. All elements support a __WODebug__ attribute. If you bind the __WODebug__ attribute to YES, the element prints messages when it resolves its bindings with its parent component. This results in logs like the following being generated:

```
[NestedList:WXNestedList] (item: {label = Alpha.2.1; value =
A.2.1; }) ==> currentItem
[NestedList:WXNestedList] (index: 0) ==> currentIndex
[NestedList:WXNestedList] sublist <== (currentItem.sublist: *nil*)
[NestedList:WXNestedList] (item: {isNew = 1; label = Alpha.2.2;
value = A.2.2; }) ==> currentItem
[NestedList:WXNestedList] (index: 1) ==> currentIndex
[NestedList:WXNestedList] sublist <== (currentItem.sublist: *nil*)
```


If you want, you can customize the messages that the elements print by overriding two methods in WOApplication. These methods are:

- __logTakeValueForDeclarationNamed:type:bindingNamed:
  associationDescription:value:__ (__logTakeValueForDeclarationNamed__ in Java)
- __logSetValueForDeclarationNamed:type:bindingNamed:
  associationDescription:value:__ (__logSetValueForDeclarationNamed__ in Java)

[!Table of Contents](Debugging%20a%20WebObjects%20Application.md) [!Next Section](Debug11.md)
