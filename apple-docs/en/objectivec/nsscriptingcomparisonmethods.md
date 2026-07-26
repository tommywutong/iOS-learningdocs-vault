---
title: NSScriptingComparisonMethods
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsscriptingcomparisonmethods
source_url: 'https://developer.apple.com/documentation/objectivec/nsscriptingcomparisonmethods'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsscriptingcomparisonmethods.json'
content_hash: 'sha256:dfc02b404fa769f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# NSScriptingComparisonMethods

<sub>API Collection</sub>

A collection of methods useful for comparing script objects.

## Overview

Often the correct way to compare two objects for scripting is different from the correct way to compare objects programmatically. This informal protocol defines a set of methods that can be implemented to perform a comparison appropriate for scripting that is independent of other methods for doing comparisons.

Cocoa scripting uses these scripting comparison methods, if available, in the process of evaluating specifier tests. If the first object being tested implements the appropriate method for the comparison operation, it will be used. If the first object doesn’t implement the appropriate method but the second object implements the inverse, the inverted comparison is performed. For example, instead of determining whether object one is less than object two, Cocoa determines whether object two is greater than object one (but only for the operations `is equal`, `is less than or equal`, `is less than`, `is greater than or equal`, or `is greater than`). If neither of the objects implements the appropriate method, Cocoa falls back on similar comparison operators in the protocol NSComparisonMethods (but again, only for the operations `is equal`, `is less than or equal`, `is less than`, `is greater than or equal`, or `is greater than`).

Cocoa provides default implementations of these scripting comparison methods for `NSString` and `NSAttributedString`. You should define implementations of these methods for any of your scriptable objects that need to perform comparisons for scripting purposes that are different than the comparisons provided by NSComparisonMethods. If none require different comparison methods, you can implement only the methods you need from `NSScriptingComparisonMethods`.

## Topics

### Performing comparisons

- [- scriptingBeginsWith:](<nsobject-swift.class/scriptingbegins(with_).md>) — Returns `true` if, in a scripting comparison, the compared object matches the beginning of `object`.
- [- scriptingContains:](<nsobject-swift.class/scriptingcontains(__).md>) — Returns `true` if, in a scripting comparison, the compared object contains `object`.
- [- scriptingEndsWith:](<nsobject-swift.class/scriptingends(with_).md>) — Returns `true` if, in a scripting comparison, the compared object matches the end of `object`.
- [- scriptingIsEqualTo:](<nsobject-swift.class/scriptingisequal(to_).md>) — Returns `true` if, in a scripting comparison, the compared object is equal to `object`.
- [- scriptingIsGreaterThan:](<nsobject-swift.class/scriptingisgreaterthan(__).md>) — Returns `true` if, in a scripting comparison, the compared object is greater than `object`.
- [- scriptingIsGreaterThanOrEqualTo:](<nsobject-swift.class/scriptingisgreaterthanorequal(to_).md>) — Returns `true` if, in a scripting comparison, the compared object is greater than or equal to `object`.
- [- scriptingIsLessThan:](<nsobject-swift.class/scriptingislessthan(__).md>) — Returns `true` if, in a scripting comparison, the compared object is less than `object`.
- [- scriptingIsLessThanOrEqualTo:](<nsobject-swift.class/scriptingislessthanorequal(to_).md>) — Returns `true` if, in a scripting comparison, the compared object is less than or equal to `object`.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
