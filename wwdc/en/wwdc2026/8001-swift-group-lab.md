---
title: Swift Group Lab
session_id: 8001
collection: wwdc2026
year: 2026
duration: '61:17'
topics: [Swift]
group: C · 并发、锁与线程
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2026/8001/'
content_hash: 'sha256:83792259f5faed83'
translated: false
---

# Swift Group Lab

<sub>WWDC2026 · 61:17 · Swift</sub>

Join us online for a deep dive into WWDC26 with Apple engineers and designers to ask questions, get advice, and follow the discussion...

> [!note] 归档理由
> Swift 实验室问答，含并发疑难（时效性一般）

## Chapters

- [Introduction](/videos/play/wwdc2026/8001/?time=0)
- [What's the best way to transfer "ownership" of non-Sendable data from one isolation domain to another without copying — e.g. an actor handing large data to another actor?](/videos/play/wwdc2026/8001/?time=273)
- [What advice and best practices (and pitfalls) do you have for using Swift structured concurrency?](/videos/play/wwdc2026/8001/?time=365)
- [Is there an overhead cost to unused/unnecessary conformances (Sendable, Equatable, Hashable, etc.) added to every struct out of habit? What happens under the hood?](/videos/play/wwdc2026/8001/?time=716)
- [Applying @MainActor triggers a massive chain reaction of async refactoring across a legacy codebase. What's the cleanest pattern to stop this 'concurrency contagion' without sacrificing Swift 6 safety?](/videos/play/wwdc2026/8001/?time=869)
- [What are the most essential modern Swift features or official resources to adopt first for high efficiency and great performance?](/videos/play/wwdc2026/8001/?time=1039)
- [After a full manual Swift 6 strict-concurrency migration, should we tear out annotations that the newer isolation model makes redundant, or leave them as no-ops?](/videos/play/wwdc2026/8001/?time=1188)
- [Why is UserDefaults not Sendable given the docs say it's thread-safe? Is this a preliminary step?](/videos/play/wwdc2026/8001/?time=1388)
- [Would it be good practice to migrate to using 'borrow/mutate' instead of 'get/set' altogether, and when would you not recommend it?](/videos/play/wwdc2026/8001/?time=1524)
- [With additions like Mutex, InlineArray, Span, typed throws, and non-copyable types, how do app developers know what's for them vs systems/embedded developers, and how do you keep up?](/videos/play/wwdc2026/8001/?time=1626)
- [Our project has very slow incremental builds with Swift Emit Module taking minutes, and splitting into modules didn't help. Can features like type inference/generics affect this, and how do we diagnose it?](/videos/play/wwdc2026/8001/?time=1917)
- [Now that Swift 6 concurrency has been adopted widely, is there anything the team would approach differently if designing it today?](/videos/play/wwdc2026/8001/?time=2019)
- [What are the notable Swift Package Manager improvements in the latest release, especially around build and dependency-resolution performance for large multi-package projects?](/videos/play/wwdc2026/8001/?time=2251)
- [What's the one Swift feature most developers don't know exists but should?](/videos/play/wwdc2026/8001/?time=2360)
- [What's left in language evolution to get tuples to finally conform to Equatable, Hashable, Comparable, etc. conditionally?](/videos/play/wwdc2026/8001/?time=2895)
- [With Swift 6 strict concurrency, what's the recommended pattern to ingest high-frequency sensor data on a background actor and stream updates to an @Observable model on the MainActor without blocking the UI?](/videos/play/wwdc2026/8001/?time=3005)
- [Performance: why is a tuple more expensive than a struct when returned from a method — or is it situational?](/videos/play/wwdc2026/8001/?time=3183)
- [What's your favorite quality-of-life / quality-of-code feature in Swift — not the obvious ones, but neat lesser-known things that make Swift fun to write?](/videos/play/wwdc2026/8001/?time=3257)

## Resources

- [Introduction](https://developer.apple.com/videos/play/wwdc2026/8001/?time=0)
- [What's the best way to transfer "ownership" of non-Sendable data from one isolation domain to another without copying — e.g. an actor handing large data to another actor?](https://developer.apple.com/videos/play/wwdc2026/8001/?time=273)
- [What advice and best practices (and pitfalls) do you have for using Swift structured concurrency?](https://developer.apple.com/videos/play/wwdc2026/8001/?time=365)
- [Is there an overhead cost to unused/unnecessary conformances (Sendable, Equatable, Hashable, etc.) added to every struct out of habit? What happens under the hood?](https://developer.apple.com/videos/play/wwdc2026/8001/?time=716)
- [Applying @MainActor triggers a massive chain reaction of async refactoring across a legacy codebase. What's the cleanest pattern to stop this 'concurrency contagion' without sacrificing Swift 6 safety?](https://developer.apple.com/videos/play/wwdc2026/8001/?time=869)
- [What are the most essential modern Swift features or official resources to adopt first for high efficiency and great performance?](https://developer.apple.com/videos/play/wwdc2026/8001/?time=1039)
- [After a full manual Swift 6 strict-concurrency migration, should we tear out annotations that the newer isolation model makes redundant, or leave them as no-ops?](https://developer.apple.com/videos/play/wwdc2026/8001/?time=1188)
- [Why is UserDefaults not Sendable given the docs say it's thread-safe? Is this a preliminary step?](https://developer.apple.com/videos/play/wwdc2026/8001/?time=1388)
- [Would it be good practice to migrate to using 'borrow/mutate' instead of 'get/set' altogether, and when would you not recommend it?](https://developer.apple.com/videos/play/wwdc2026/8001/?time=1524)
- [With additions like Mutex, InlineArray, Span, typed throws, and non-copyable types, how do app developers know what's for them vs systems/embedded developers, and how do you keep up?](https://developer.apple.com/videos/play/wwdc2026/8001/?time=1626)
- [Our project has very slow incremental builds with Swift Emit Module taking minutes, and splitting into modules didn't help. Can features like type inference/generics affect this, and how do we diagnose it?](https://developer.apple.com/videos/play/wwdc2026/8001/?time=1917)
- [Now that Swift 6 concurrency has been adopted widely, is there anything the team would approach differently if designing it today?](https://developer.apple.com/videos/play/wwdc2026/8001/?time=2019)
- [What are the notable Swift Package Manager improvements in the latest release, especially around build and dependency-resolution performance for large multi-package projects?](https://developer.apple.com/videos/play/wwdc2026/8001/?time=2251)
- [What's the one Swift feature most developers don't know exists but should?](https://developer.apple.com/videos/play/wwdc2026/8001/?time=2360)
- [What's left in language evolution to get tuples to finally conform to Equatable, Hashable, Comparable, etc. conditionally?](https://developer.apple.com/videos/play/wwdc2026/8001/?time=2895)
- [With Swift 6 strict concurrency, what's the recommended pattern to ingest high-frequency sensor data on a background actor and stream updates to an @Observable model on the MainActor without blocking the UI?](https://developer.apple.com/videos/play/wwdc2026/8001/?time=3005)
- [Performance: why is a tuple more expensive than a struct when returned from a method — or is it situational?](https://developer.apple.com/videos/play/wwdc2026/8001/?time=3183)
- [What's your favorite quality-of-life / quality-of-code feature in Swift — not the obvious ones, but neat lesser-known things that make Swift fun to write?](https://developer.apple.com/videos/play/wwdc2026/8001/?time=3257)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/8001/1/6ee7f28d-d198-4690-af7e-ac35f4173c3c/downloads/wwdc2026-8001_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/8001/1/6ee7f28d-d198-4690-af7e-ac35f4173c3c/downloads/wwdc2026-8001_sd.mp4?dl=1)

> [!warning] 本场没有可用的逐字稿。
