---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Protocols/EOAdaptorDelegate.html
archived_at: '2026-07-15T08:11:35.974131Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOAdaptor Delegate

> __(informal protocol)__

> __Declared in:__  EOAccess/EOAdaptor.h

## Protocol Description

---

The delegate for EOAdaptor can implement the method [adaptor:fetchedValueForValue:attribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpoiqeizlmmvtwc5dff5qwiylqorxxeotgmv2gg2dfmrlgc3dvmvdg64swmfwhkzj2mf2hi4tjmj2xizj2) to perform
a database-specific transformations on a value.

## Instance Methods

---

### adaptor:fetchedValueForValue:attribute:

`- (id)adaptor:(EOAdaptor
*)adaptor
fetchedValueForValue:(id)value
attribute:(EOAttribute *)attribute`

Invoked from [fetchedValueForValue:attribute:](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwmzlumnugkzcwmfwhkzkgn5zfmylmovstuyluorzgsytvorstu) to
allow the delegate to perform a database-specific transformation
on _value_. The delegate should return
the value that the adaptor's database server would ultimately
store for _value_ if it was inserted
or updated in the column described by _attribute._

Ordinarily, [fetchedValueForValue:attribute:](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwmzlumnugkzcwmfwhkzkgn5zfmylmovstuyluorzgsytvorstu) invokes
one of the type-specific __fetchedValue...__ methods
depending on the type of _value_. If
you implement this delegate method, [fetchedValueForValue:attribute:](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwmzlumnugkzcwmfwhkzkgn5zfmylmovstuyluorzgsytvorstu) does
not invoke the other __fetchedValue...__ methods.
It simply invokes your delegate method and returns the value returned
from it. Therefore, an implementation of [adaptor:fetchedValueForValue:attribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpoiqeizlmmvtwc5dff5qwiylqorxxeotgmv2gg2dfmrlgc3dvmvdg64swmfwhkzj2mf2hi4tjmj2xizj2) must
handle values of all types.

---

### reconnectionDictionaryForAdaptor:

`- (NSDictionary *)reconnectionDictionaryForAdaptor:(EOAdaptor
*)adaptor`

Invoked from [handleDroppedConnection](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwqylomrwgkrdsn5yhazleinxw43tfmn2gs33o) to provides
a new connection dictionary for reconnection attempts. If the adaptor's
database connection is dropped (and the adaptor supports database reconnection),
the adaptor attempts to recover by reconnecting. By default, the
adaptor attempts to connect using its original connection dictionary.
If you want it to connect to a different database, implement this
method to return a connection dictionary for the secondary database.
(Note that the secondary database should have the same data as the
original.) If the delegate method is not implemented, the adaptor
uses its existing connection dictionary to reconnect to the server.

__See Also:__
[- isDroppedConnectionException:](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixws42eojxxa4dfmrbw63tomvrxi2lpnzcxqy3fob2gs33ohi)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
