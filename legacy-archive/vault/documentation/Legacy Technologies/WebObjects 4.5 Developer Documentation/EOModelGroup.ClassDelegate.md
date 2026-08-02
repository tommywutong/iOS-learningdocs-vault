---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Protocols/EOModelGroupClassDelegate.html
archived_at: '2026-07-15T08:11:33.248099Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOModelGroup.ClassDelegate

> __(informal interface)__

> __Package:__
> com.apple.yellow.eoaccess

## Interface Description

---

An EOModelGroup object should have a delegate which can influence
how it finds and loads models. In addition to the delegates you
assign to EOModelGroup instances, the EOModelGroup class itself
can have a delegate. The class delegate implements a single method- [defaultModelGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjvxwizlmi5zg65lqfzbwyyltoncgk3dfm5qxizjpmrswmylvnr2e233emvweo4tpovya).

For more information on EOModelGroup instance delegate methods,
see the [EOModelGroup.Delegate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Protocols/EOModelGroupDelegate.html#CBACDGDA) interface specification.

## Instance Methods

---

### defaultModelGroup

`public abstract EOModelGroup defaultModelGroup()`

If implemented by the EOModelGroup class delegate,
this method should return the EOModelGroup to be returned in response
to the message __defaultModelGroup__. If this
delegate method returns null, EOModelGroup uses the default behavior
of the __defaultModelGroup__ class method.
Note that this method is implemented by the delegate assigned to
the EOModelGroup class object.

__See Also:__
[classDelegate](EOModelGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3dnrqxg42emvwgkz3borsq) (EOModelGroup
class), [setClassDelegate](EOModelGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6tlpmrswyr3sn52xal3tmv2eg3dbonzuizlmmvtwc5df) (EOModelGroup
class)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
