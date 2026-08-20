---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EORadioMatrixAssociation.html
archived_at: '2026-07-18T01:28:43.869450Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOPopUpAssociation.md)
[!](EORecursiveBrowserAssociation.md)

---

# EORadioMatrixAssociation

__Inherits From:__
EOAssociation : EODelayedObserver : NSObject

EOObserving (EODelayedObserver)

__Inherits From:__
com.apple.yellow.eointerface (Yellow Box)

---

## Class Description

EORadioMatrixAssociation displays a string or an integer in an NSMatrix. EORadioMatrixAssociation includes three aspects: `selectedTitle`, which is useful for values representable as strings; `selectedTag`, for integer values; and __enabled__  for enabling and disabling the NSMatrix.

EORadioMatrixAssociation is for use in Yellow Box applications only; there isn't an equivalent class for Java Client.

**---

### Purpose**

An EORadioMatrixAssociation binds titles or tags of controls in an NSMatrix to string or integer attributes.

```
```

| __Aspects__ | __Aspects__ |
| selectedTitle | An attribute of the selected object whose values can be represented as strings. |
| selectedTag | An integer attribute of the selected object. |
| enabled | A boolean attribute of the selected object, which determines whether the matrix is enabled. |

```
```

| __Object Keys Taken__ | __Object Keys Taken__ |
| target | When the user chooses an item in the matrix, the EORadioMatrixAssociation updates the selected object's property with the item's title or tag. |

```
```


---

## Instance Methods

---

### setTagValueForOther:

public void `setTagValueForOther`(int _tag_)

Records _tag_ as the "unknown" tag. When a property value doesn't match any other tag in the matrix, the EORadioMatrixAssociation automatically selects the item for this tag. If there's no item for this tag, the radio button selection isn't changed. This tag value is by default -1.

---

### tagValueForOther

public int `tagValueForOther`()

Returns the "unknown" tag.

---

[!](EOPopUpAssociation.md)
[!](EORecursiveBrowserAssociation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
