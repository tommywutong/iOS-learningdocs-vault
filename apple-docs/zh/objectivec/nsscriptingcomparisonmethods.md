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
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# NSScriptingComparisonMethods

<sub>API 集合</sub>

一组用于比较脚本对象的方法。

## Overview

为脚本编写目的而比较两个对象的正确方式，往往与以编程方式比较对象的正确方式不同。这个非正式协议定义了一组方法，可以实现这些方法来执行适合脚本编写的比较，且独立于其他用于比较的方法。

在求值说明符测试的过程中，如果可用，Cocoa 脚本编写会使用这些脚本比较方法。如果被测试的第一个对象实现了该比较操作对应的方法，就会使用它。如果第一个对象没有实现对应的方法，但第二个对象实现了其反向操作，就会执行反转后的比较。例如，Cocoa 不会去判断对象一是否小于对象二，而是判断对象二是否大于对象一（但这仅适用于 `is equal`、`is less than or equal`、`is less than`、`is greater than or equal` 或 `is greater than` 这些操作）。如果两个对象都没有实现相应的方法，Cocoa 会回退使用协议 NSComparisonMethods 中类似的比较运算符（同样，也仅适用于 `is equal`、`is less than or equal`、`is less than`、`is greater than or equal` 或 `is greater than` 这些操作）。

Cocoa 为 `NSString` 和 `NSAttributedString` 提供了这些脚本比较方法的默认实现。对于任何需要执行与 NSComparisonMethods 所提供的比较不同的、面向脚本编写的比较的可脚本化对象，你都应该定义这些方法的实现。如果没有对象需要不同的比较方法，你可以只实现 `NSScriptingComparisonMethods` 中你需要的那些方法。

## Topics

### Performing comparisons

- [- scriptingBeginsWith:](<nsobject-swift.class/scriptingbegins(with_).md>) — 在脚本比较中，如果被比较的对象与 `object` 的开头匹配，则返回 `true`。
- [- scriptingContains:](<nsobject-swift.class/scriptingcontains(__).md>) — 在脚本比较中，如果被比较的对象包含 `object`，则返回 `true`。
- [- scriptingEndsWith:](<nsobject-swift.class/scriptingends(with_).md>) — 在脚本比较中，如果被比较的对象与 `object` 的结尾匹配，则返回 `true`。
- [- scriptingIsEqualTo:](<nsobject-swift.class/scriptingisequal(to_).md>) — 在脚本比较中，如果被比较的对象等于 `object`，则返回 `true`。
- [- scriptingIsGreaterThan:](<nsobject-swift.class/scriptingisgreaterthan(__).md>) — 在脚本比较中，如果被比较的对象大于 `object`，则返回 `true`。
- [- scriptingIsGreaterThanOrEqualTo:](<nsobject-swift.class/scriptingisgreaterthanorequal(to_).md>) — 在脚本比较中，如果被比较的对象大于或等于 `object`，则返回 `true`。
- [- scriptingIsLessThan:](<nsobject-swift.class/scriptingislessthan(__).md>) — 在脚本比较中，如果被比较的对象小于 `object`，则返回 `true`。
- [- scriptingIsLessThanOrEqualTo:](<nsobject-swift.class/scriptingislessthanorequal(to_).md>) — 在脚本比较中，如果被比较的对象小于或等于 `object`，则返回 `true`。

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
