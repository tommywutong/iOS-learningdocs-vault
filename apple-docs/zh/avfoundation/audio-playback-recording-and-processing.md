---
title: 音频播放、录制与处理
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/audio-playback-recording-and-processing
source_url: 'https://developer.apple.com/documentation/avfoundation/audio-playback-recording-and-processing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/audio-playback-recording-and-processing.json'
content_hash: 'sha256:769f4caf4e02551e'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md)

# 音频播放、录制与处理

播放、录制和处理音频；配置你的 App 的系统音频行为。

## 主题

### 系统音频

- [处理音频中断](../avfaudio/handling-audio-interruptions.md) — 观察音频会话通知，确保你的 App 恰当地响应中断。
- [响应音频路由变化](../avfaudio/responding-to-audio-route-changes.md) — 观察音频会话通知，确保你的 App 恰当地响应路由变化。
- [从内置麦克风捕获立体声音频](../avfaudio/capturing-stereo-audio-from-built-in-microphones.md) — 配置 iOS 设备的内置麦克风，为你的 App 添加立体声录音能力。
- [AVAudioSession](../avfaudio/avaudiosession.md) — 一个向系统传达你打算如何在 App 中使用音频的对象。
- [AVAudioApplication](../avfaudio/avaudioapplication.md) — 一个管理属于某个 App 的一个或多个音频会话的对象。
- [AVAudioRoutingArbiter](../avfaudio/avaudioroutingarbiter.md) — 一个用于配置 macOS App 以参与 AirPods 自动切换的对象。

### 基本播放与录制

- [AVAudioPlayer](../avfaudio/avaudioplayer.md) — 一个从文件或缓冲区播放音频数据的对象。
- [AVAudioRecorder](../avfaudio/avaudiorecorder.md) — 一个将音频数据录制到文件的对象。
- [AVMIDIPlayer](../avfaudio/avmidiplayer.md) — 一个通过系统声音模块播放 MIDI 数据的对象。

### 高级音频处理

- [音频引擎](../avfaudio/audio-engine.md) — 执行高级实时和离线音频处理、实现 3D 空间化，以及使用 MIDI 和采样器。

## 另请参阅

### 音频

- [语音合成](speech-synthesis.md) — 配置语音以朗读文本字符串。
