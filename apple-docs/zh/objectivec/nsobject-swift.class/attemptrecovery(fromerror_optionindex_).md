---
title: 'attemptRecovery(fromError:optionIndex:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/attemptrecovery(fromerror:optionindex:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/attemptrecovery(fromerror:optionindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/attemptrecovery%28fromerror%3Aoptionindex%3A%29.json'
content_hash: 'sha256:93ee6b43ee00f916'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# attemptRecovery(fromError:optionIndex:)

<sub>实例方法</sub>

实现此方法以尝试从应用模态对话框中指出的错误中恢复。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func attemptRecovery(fromError error: any Error, optionIndex recoveryOptionIndex: Int) -> Bool
```

## 参数

- `error` — 描述错误（包括错误恢复选项）的 [NSError](../../foundation/nserror.md) 对象。

- `recoveryOptionIndex` — 用户在 `error` 的本地化恢复数组中所选恢复选项的索引。

## 返回值

如果错误恢复成功完成，则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 讨论

当已在应用模态对话框中向用户呈现错误警报，且用户选择了 `error` 指定的错误恢复选项时调用。
