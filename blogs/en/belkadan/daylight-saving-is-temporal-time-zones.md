---
title: Daylight Saving Is Temporal Time Zones
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2023/12/Daylight-Saving-Is-Temporal-Time-Zones/'
original_language: en
published: 2023-12-13
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bc367b8761ef9c74'
translated: false
---

> 原文：[Daylight Saving Is Temporal Time Zones](https://belkadan.com/blog/2023/12/Daylight-Saving-Is-Temporal-Time-Zones/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [GitMounter](https://belkadan.com/blog/2023/11/GitMounter/)

[Protobuf Is Almost Streamable](https://belkadan.com/blog/2023/12/Protobuf-Is-Almost-Streamable/) »

## [Daylight Saving Is Temporal Time Zones](#)

- offset applied to UTC to get to local time
- that depends on your position {on Earth, in orbit around the sun}
- approximating a natural difference in available sunlight
- rules have changed in the past and probably will in the future
- for political reasons

Further reading:

- qntm’s “[So You Want Continuous Time Zones](https://qntm.org/continuous)”
- qntm’s “[So You Want To Abolish Time Zones](https://qntm.org/abolish)”
- Dave DeLong’s “[Your Calendrical Fallicy Is…](https://yourcalendricalfallacyis.com)”

[![xkcd: "Event 1 happened at time T1. Event 2 happened at time T2. How would you calculate how much time elapsed between T1 and T2? Normal answer: T2 minus T1. Anyone who's worked on DateTime systems: IT IS IMPOSSIBLE TO KNOW AND A SIN TO ASK!"](https://imgs.xkcd.com/comics/datetime.png)](https://xkcd.com/2867)

This entry was posted on [December](https://belkadan.com/blog/2023/12) 13, [2023](https://belkadan.com/blog/2023) and is filed under [Technical](https://belkadan.com/blog/technical).
