---
title: 'attemptRecovery(fromError:optionIndex:delegate:didRecoverSelector:contextInfo:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/attemptrecovery(fromerror:optionindex:delegate:didrecoverselector:contextinfo:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/attemptrecovery(fromerror:optionindex:delegate:didrecoverselector:contextinfo:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/attemptrecovery%28fromerror%3Aoptionindex%3Adelegate%3Adidrecoverselector%3Acontextinfo%3A%29.json'
content_hash: 'sha256:69c4e2e8f82499df'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# attemptRecovery(fromError:optionIndex:delegate:didRecoverSelector:contextInfo:)

<sub>实例方法</sub>

实现此方法以尝试从文稿模态 sheet 中指出的错误中恢复。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func attemptRecovery(fromError error: any Error, optionIndex recoveryOptionIndex: Int, delegate: Any?, didRecoverSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

## 参数

- `error` — 描述错误（包括错误恢复选项）的 [NSError](../../foundation/nserror.md) 对象。

- `recoveryOptionIndex` — 用户在 `error` 的本地化恢复数组中所选恢复选项的索引。

- `delegate` — 作为模态委托的对象。

- `didRecoverSelector` — 标识模态委托所实现方法的选择器。

- `contextInfo` — 与错误恢复尝试关联的任意数据，将在 `didRecoverSelector` 中传递给 `delegate`。

## 讨论

当在文稿模态 sheet 中向用户呈现错误警报，且用户选择了 `error` 指定的错误恢复选项时调用。尝试恢复后，你的实现应向 `delegate` 发送 `didRecoverSelector` 中指定的消息，并传入所提供的 `contextInfo`。

`didRecoverSelector` 应具有以下签名：

```objc
- (void)didPresentErrorWithRecovery:(BOOL)didRecover contextInfo:(void *)contextInfo;
```

其中，如果错误恢复尝试成功，则 `didRecover` 为 [YES](../yes.md)；否则为 [NO](../no.md)。
