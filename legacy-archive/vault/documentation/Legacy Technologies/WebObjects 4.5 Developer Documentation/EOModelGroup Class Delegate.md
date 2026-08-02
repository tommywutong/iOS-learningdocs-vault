---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Protocols/EOModelGroupClassDelegate.html
archived_at: '2026-07-15T08:11:36.032235Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOModelGroup Class Delegate

> __(informal protocol)__

> __Declared in:__  EOAccess/EOModelGroup.h

## Protocol Description

---

An EOModelGroup object should have a delegate which can influence
how it finds and loads models. In addition to the delegates you
assign to EOModelGroup instances, the EOModelGroup class itself
can have a delegate. The class delegate implements a single method- [defaultModelGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2nn5sgk3chojxxk4bainwgc43tebcgk3dfm5qxizjpmrswmylvnr2e233emvweo4tpovya).

For more information on EOModelGroup instance delegate methods,
see the [EOModelGroup Delegate](EOModelGroup%20Delegate.md#apple-inbecq2ei5cec) protocol specification.

## Instance Methods

---

### defaultModelGroup

`- (EOModelGroup *)defaultModelGroup`

If implemented by the EOModelGroup class delegate,
this method should return the EOModelGroup to be returned in response
to the message __defaultModelGroup__. If this
delegate method returnsnil, EOModelGroup uses the default behavior
of the __defaultModelGroup__ class method.
Note that this method is implemented by the delegate assigned to
the EOModelGroup class object.

__See Also:__
[+ classDelegate](EOModelGroup-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc6y3mmfzxgrdfnrswoylumu) (EOModelGroup
class), [+ setClassDelegate:](EOModelGroup-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc643forbwyyltoncgk3dfm5qxizj2) (EOModelGroup
class)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
