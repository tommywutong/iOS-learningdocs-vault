---
title: 语音合成
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/speech-synthesis
source_url: 'https://developer.apple.com/documentation/avfoundation/speech-synthesis'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/speech-synthesis.json'
content_hash: 'sha256:350a1d1be25e649b'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md)

# 语音合成

配置语音以朗读文本字符串。

## 概述

语音合成（Speech Synthesis）框架管理语音和语音合成，需要完成两个主要任务：

创建一个包含要朗读文本的 [AVSpeechUtterance](../avfaudio/avspeechutterance.md) 实例。你可以选择为每个发声话语配置语音参数，例如语音和速率。

```swift
// 创建一个话语。
let utterance = AVSpeechUtterance(string: "The quick brown fox jumped over the lazy dog.")

// 配置该话语。
utterance.rate = 0.57
utterance.pitchMultiplier = 0.8
utterance.postUtteranceDelay = 0.2
utterance.volume = 0.8

// 获取英式英语语音。
let voice = AVSpeechSynthesisVoice(language: "en-GB")

// 将语音指定给该话语。
utterance.voice = voice
```

将该话语传递给一个 [AVSpeechSynthesizer](../avfaudio/avspeechsynthesizer.md) 实例以生成朗读音频。

```swift
// 创建一个语音合成器。
let synthesizer = AVSpeechSynthesizer()

// 让合成器朗读该话语。
synthesizer.speak(utterance)
```

你还可以选择使用这个语音合成器实例来控制或响应正在进行的语音；例如，指定它的 [delegate](../avfaudio/avspeechsynthesizer/delegate.md) 以接收语音事件通知。

> [!note] 注意
> 语音生成在设备端进行，不会发送到服务器处理。

## 主题

### 朗读文本属性

- [AVSpeechUtterance](../avfaudio/avspeechutterance.md) — 一个封装用于语音合成的文本以及影响语音效果的参数的对象。
- [AVSpeechSynthesisVoice](../avfaudio/avspeechsynthesisvoice.md) — 用于语音合成的独特语音。

### 语音合成控制

- [AVSpeechSynthesizer](../avfaudio/avspeechsynthesizer.md) — 一个从文本话语生成合成语音的对象，支持监控或控制正在进行的语音。

### 语音合成音频单元

- [AVSpeechSynthesisProviderAudioUnit](../avfaudio/avspeechsynthesisprovideraudiounit.md) — 一个从文本生成语音的对象。

## 另请参阅

### 音频

- [音频播放、录制与处理](audio-playback-recording-and-processing.md) — 播放、录制和处理音频；配置你的 App 的系统音频行为。
