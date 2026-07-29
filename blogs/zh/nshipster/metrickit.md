---
title: MetricKit
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/metrickit/'
original_language: en
published: 2019-10-21
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:43f323b7c66e252d'
translated: true
---

> 原文：[MetricKit](https://nshipster.com/metrickit/)　·　NSHipster (Mattt)

# [Metric​Kit](https://nshipster.com/metrickit/)

作者：[Mattt](https://nshipster.com/authors/mattt/)　　2019 年 10 月 21 日

本科的时候，我在电台做一档叫 _《Goodbye, Blue Monday》_ 的节目（当时我特别迷冯内古特）。节目没什么了不起的——只是每周在电台切换到自动播控之前的深夜时段，有 2 个小时的档期。

如果你在深夜开车穿越宾夕法尼亚州匹兹堡的山丘，恰巧把收音机调到 [WRCT 88.3](http://www.wrct.org)，你会听到混杂在一起的[当代古典](https://beta.music.apple.com/us/album/acoustica/410402556)、[酸爵士](https://beta.music.apple.com/us/album/a-funk-odyssey/203132910)、[意大利迪斯科](https://beta.music.apple.com/us/album/ma-quale-idea-single/1415038751)和[比波普](https://beta.music.apple.com/us/album/kind-of-blue/268443092)。还有，一个大学生尽力模仿 [Tony Mowod](http://old.post-gazette.com/magazine/20010404mowod4.asp) 的、带着拿腔拿调的悦耳男中音。

坐在播控室里，等着曲子播完，然后播一段 FCC 规定的公益广告或者整点[电台识别](https://en.wikipedia.org/wiki/Station_identification)，我常常会想：_到底有没有人在听？_ _就算有人在听，他们喜欢吗？_ 也许我一直在播静电噪音，自己却浑然不知。

每次向 App Store Connect 提交构建时，我也会有同样的想法……但随后我会想起，和电台不同，你_确实_可以知道这些！而 Xcode 11 的最新改进，让你比以往更容易了解你的 App 在实际环境中的表现。

关于这方面你需要知道的一切，我们都会在 NSHipster 本周的文章里覆盖。就像电台里说的那样：_“请不要扭动旋钮（上面沾了果酱）。”_

---

MetricKit 是 iOS 13 中用于收集和处理电池与性能指标的一个新框架（framework）。它在[今年的 WWDC](https://nshipster.com/wwdc-2019/) 上与 XCTest Metrics 和 Xcode Metrics Organizer 一同发布，作为一项协同努力的一部分，旨在让开发者更深入地了解他们的 App 在实际环境中的表现。

![MetricKit 示意图](https://nshipster.com/assets/metrickit-diagram--light-7ec04a565bf8ee06d0b61aa9784804981ade0eaa1581727c4302fcba07281bf4a6c3cc650145092dae446b915ae159afb29baf5af531f46c650028e7853e51e4.png)

<sub>来自 WWDC 2019 Session 417 的示意图：[《Improving Battery Life and Performance》](https://developer.apple.com/videos/play/wwdc2019/417/)</sub>

Apple 会自动从 App Store 安装的 App 中收集指标。你可以在 Xcode 11 中通过打开 Organizer（⌥⌘⇧O）并选择新的 Metrics 标签页来查看它们。

MetricKit 对 Xcode Organizer Metrics 进行了补充，提供了一种编程方式，每天接收关于你的 App 在实际环境中表现的信息。有了这些信息，你可以比通过 Xcode 更详细地自行收集、聚合和分析。

## 了解 App 指标

指标可以帮助你发现本地测试时可能未注意到的问题，并让你能够跟踪不同版本 App 之间的变化。在本次初始版本中，Apple 重点关注了对用户最重要的两个指标：电池用量和性能。

### 电池用量

![MetricKit 电池用量示意图](https://nshipster.com/assets/metrickit-battery-usage--light-ab6e3a8651c208bb04d13d92ef81b9bb31326e868c8a521a1f348c7e4b735bffa276f7bece2d44ff4aeabecae04a054bf345f27d1bda27ae4eb8bde1d8937629.png)

电池续航取决于很多不同因素。设备的老化程度和充电循环次数等物理因素是决定性的，但手机的使用方式也很重要。诸如 CPU 使用率、屏幕亮度和屏幕上的颜色、以及无线电设备获取数据或获取你当前位置的频率等——所有这些都可能造成很大影响。但最需要记住的是，用户非常在意电池续航。

除了相机好不好的问题外，如今人们购买新手机时的决定性因素就是两次充电之间的时间间隔。所以当他们昂贵的新手机_撑不过_一天时，他们会非常不高兴。

直到最近，Apple 在电池问题上一直是首当其冲。但自 iOS 12 以来，设置中的新[电池用量屏幕](https://support.apple.com/en-us/HT201264)让用户现在可以判断出何时是他们最喜欢的 App 在作祟。幸运的是，借助 iOS 13，你现在拥有了确保你的 App 不会违反合理能耗所需的一切。

### 性能

性能是整体用户体验中的另一个关键因素。通常，我们可能将处理器时钟速度或[帧率](https://nshipster.com/uitableviewheaderfooterview/)之类的统计数据作为性能的衡量标准。但相反，Apple 关注的是更具体、更可操作的指标：

挂起率（Hang Rate） 主线程 / UI 线程被阻塞，导致 App 无法响应用户输入的频率是多少？启动时间（Launch Time） 用户在点击 App 图标后，App 需要多长时间才能变得可用？峰值内存与挂起时内存（Peak Memory & Memory at Suspension） App 在其峰值时以及即将进入后台前的内存用量是多少？磁盘写入（Disk Writes） App 写入磁盘的频率有多高——如果你还不知道的话——这是一个[相对慢速的操作](https://people.eecs.berkeley.edu/~rcs/research/interactive_latency.html) _（即使是在 iPhone 的闪存存储上！）_

## 使用 MetricKit

从 API 使用者的角度来看，很难想象 MetricKit 能更容易集成。你只需要让你的 App 的某个部分充当指标订阅者（一个显而易见的选择是你的 `AppDelegate`），并将其添加到共享的 `MXMetricManager` 中：

```
import UIKit
import MetricKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        MXMetricManager.shared.add(self)
        return true
    }

    func applicationWillTerminate(_ application: UIApplication) {
        MXMetricManager.shared.remove(self)
    }
}

extension AppDelegate: MXMetricManagerSubscriber {
    func didReceive(_ payloads: [MXMetricPayload]) {
        ...
    }
}
```

iOS 会在你的 App 被使用时自动收集样本，并且每天一次（每 24 小时），它会发送一份包含这些指标的聚合报告。

要验证你的 `MXMetricManagerSubscriber` 的委托方法是否按预期被调用，请在 Xcode 运行你的 App 时，从 Debug 菜单中选择 Simulate MetricKit Payloads。

### 使用 Signpost 注释关键代码段

除了为你收集的基线统计数据外，你还可以使用 [`mxSignpost`](https://developer.apple.com/documentation/metrickit/3214364-mxsignpost) 函数来收集围绕代码中最重要部分的指标。这个由 [signpost](https://developer.apple.com/documentation/os/3019241-os_signpost) 驱动的 API 可以捕获 CPU 时间、内存和磁盘写入。

例如，如果你的 App 的一部分对音频流执行了后期处理，你可以使用 metric signpost 注释这些区域，以确定该工作的能耗和性能影响：

```
let audioLogHandle = MXMetricManager.makeLogHandle(category: "Audio")

func processAudioStream() {
    mxSignpost(.begin, log: audioLogHandle, name: "ProcessAudioStream")
    …
    mxSignpost(.end, log: audioLogHandle, name: "ProcessAudioStream")
}
```

## 创建用于收集 App 指标的自托管 Web 服务

现在你已经有了这些信息，你该怎么处理它？我们如何填充 `…` 实现中的那个 `didReceive(_:)` 占位符？

你_可以_把这些传递给某个付费的分析或崩溃报告服务，_但这有什么乐趣呢_？让我们构建自己的 Web 服务来收集这些信息，以便进行进一步分析：

### 使用 PostgreSQL 存储和查询指标

指标管理器订阅者接收到的 `MXMetricPayload` 对象有一个方便的 [`jsonRepresentation()`](https://developer.apple.com/documentation/metrickit/mxmetricpayload/3131907-jsonrepresentation) 方法，可以生成如下所示的内容：

展开以查看 JSON 表示：

```
{
  "locationActivityMetrics": {
    "cumulativeBestAccuracyForNavigationTime": "20 sec",
    "cumulativeBestAccuracyTime": "30 sec",
    "cumulativeHundredMetersAccuracyTime": "30 sec",
    "cumulativeNearestTenMetersAccuracyTime": "30 sec",
    "cumulativeKilometerAccuracyTime": "20 sec",
    "cumulativeThreeKilometersAccuracyTime": "20 sec"
  },
  "cellularConditionMetrics": {
    "cellConditionTime": {
      "histogramNumBuckets": 3,
      "histogramValue": {
        "0": {
          "bucketCount": 20,
          "bucketStart": "1 bars",
          "bucketEnd": "1 bars"
        },
        "1": {
          "bucketCount": 30,
          "bucketStart": "2 bars",
          "bucketEnd": "2 bars"
        },
        "2": {
          "bucketCount": 50,
          "bucketStart": "3 bars",
          "bucketEnd": "3 bars"
        }
      }
    }
  },
  "metaData": {
    "appBuildVersion": "0",
    "osVersion": "iPhone OS 13.1.3 (17A878)",
    "regionFormat": "US",
    "deviceType": "iPhone9,2"
  },
  "gpuMetrics": {
    "cumulativeGPUTime": "20 sec"
  },
  "memoryMetrics": {
    "peakMemoryUsage": "200,000 kB",
    "averageSuspendedMemory": {
      "averageValue": "100,000 kB",
      "standardDeviation": 0,
      "sampleCount": 500
    }
  },
  "signpostMetrics": [
    {
      "signpostIntervalData": {
        "histogrammedSignpostDurations": {
          "histogramNumBuckets": 3,
          "histogramValue": {
            "0": {
              "bucketCount": 50,
              "bucketStart": "0 ms",
              "bucketEnd": "100 ms"
            },
            "1": {
              "bucketCount": 60,
              "bucketStart": "100 ms",
              "bucketEnd": "400 ms"
            },
            "2": {
              "bucketCount": 30,
              "bucketStart": "400 ms",
              "bucketEnd": "700 ms"
            }
          }
        },
        "signpostCumulativeCPUTime": "30,000 ms",
        "signpostAverageMemory": "100,000 kB",
        "signpostCumulativeLogicalWrites": "600 kB"
      },
      "signpostCategory": "TestSignpostCategory1",
      "signpostName": "TestSignpostName1",
      "totalSignpostCount": 30
    },
    {
      "signpostIntervalData": {
        "histogrammedSignpostDurations": {
          "histogramNumBuckets": 3,
          "histogramValue": {
            "0": {
              "bucketCount": 60,
              "bucketStart": "0 ms",
              "bucketEnd": "200 ms"
            },
            "1": {
              "bucketCount": 70,
              "bucketStart": "201 ms",
              "bucketEnd": "300 ms"
            },
            "2": {
              "bucketCount": 80,
              "bucketStart": "301 ms",
              "bucketEnd": "500 ms"
            }
          }
        },
        "signpostCumulativeCPUTime": "50,000 ms",
        "signpostAverageMemory": "60,000 kB",
        "signpostCumulativeLogicalWrites": "700 kB"
      },
      "signpostCategory": "TestSignpostCategory2",
      "signpostName": "TestSignpostName2",
      "totalSignpostCount": 40
    }
  ],
  "displayMetrics": {
    "averagePixelLuminance": {
      "averageValue": "50 apl",
      "standardDeviation": 0,
      "sampleCount": 500
    }
  },
  "cpuMetrics": {
    "cumulativeCPUTime": "100 sec"
  },
  "networkTransferMetrics": {
    "cumulativeCellularDownload": "80,000 kB",
    "cumulativeWifiDownload": "60,000 kB",
    "cumulativeCellularUpload": "70,000 kB",
    "cumulativeWifiUpload": "50,000 kB"
  },
  "diskIOMetrics": {
    "cumulativeLogicalWrites": "1,300 kB"
  },
  "applicationLaunchMetrics": {
    "histogrammedTimeToFirstDrawKey": {
      "histogramNumBuckets": 3,
      "histogramValue": {
        "0": {
          "bucketCount": 50,
          "bucketStart": "1,000 ms",
          "bucketEnd": "1,010 ms"
        },
        "1": {
          "bucketCount": 60,
          "bucketStart": "2,000 ms",
          "bucketEnd": "2,010 ms"
        },
        "2": {
          "bucketCount": 30,
          "bucketStart": "3,000 ms",
          "bucketEnd": "3,010 ms"
        }
      }
    },
    "histogrammedResumeTime": {
      "histogramNumBuckets": 3,
      "histogramValue": {
        "0": {
          "bucketCount": 60,
          "bucketStart": "200 ms",
          "bucketEnd": "210 ms"
        },
        "1": {
          "bucketCount": 70,
          "bucketStart": "300 ms",
          "bucketEnd": "310 ms"
        },
        "2": {
          "bucketCount": 80,
          "bucketStart": "500 ms",
          "bucketEnd": "510 ms"
        }
      }
    }
  },
  "applicationTimeMetrics": {
    "cumulativeForegroundTime": "700 sec",
    "cumulativeBackgroundTime": "40 sec",
    "cumulativeBackgroundAudioTime": "30 sec",
    "cumulativeBackgroundLocationTime": "30 sec"
  },
  "timeStampEnd": "2019-10-22 06:59:00 +0000",
  "applicationResponsivenessMetrics": {
    "histogrammedAppHangTime": {
      "histogramNumBuckets": 3,
      "histogramValue": {
        "0": {
          "bucketCount": 50,
          "bucketStart": "0 ms",
          "bucketEnd": "100 ms"
        },
        "1": {
          "bucketCount": 60,
          "bucketStart": "100 ms",
          "bucketEnd": "400 ms"
        },
        "2": {
          "bucketCount": 30,
          "bucketStart": "400 ms",
          "bucketEnd": "700 ms"
        }
      }
    }
  },
  "appVersion": "1.0.0",
  "timeStampBegin": "2019-10-21 07:00:00 +0000"
}
```

正如你所看到的，这个表示中包含了大量信息。为所有这些信息定义 schema 将是一项艰巨的工作，而且无法保证这在未来不会发生变化。因此，让我们拥抱 NoSQL 范式 _（尽管要负责任地，使用 [Postgres](https://postgresapp.com)）_，将 payload 存储在 [`JSONB` 列](https://www.postgresql.org/docs/current/datatype-json.html)中：

```
CREATE TABLE IF NOT EXISTS metrics (
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    payload JSONB NOT NULL
);
```

_太简单了！_

我们可以使用 [JSON 操作符](https://www.postgresql.org/docs/current/functions-json.html)从 payload 中提取单个字段，如下所示：

```
SELECT (payload -> 'applicationTimeMetrics'
                ->> 'cumulativeForegroundTime')::INTERVAL
FROM metrics;
--      interval
-- ═══════════════════
--  @ 11 mins 40 secs
-- (1 row)
```

#### 进阶：创建视图

PostgreSQL 中的 JSON 操作符使用起来可能很繁琐——尤其是在进行更复杂的查询时。一个有用的方法是创建一个视图（[物化视图](https://www.postgresql.org/docs/current/rules-materializedviews.html)或其他类型），以最方便的形式为你投射出最重要的信息：

```
CREATE VIEW key_performance_indicators AS
SELECT
    id,
    (payload -> 'appVersion') AS app_version,
    (payload -> 'metaData' ->> 'deviceType') AS device_type,
    (payload -> 'metaData' ->> 'regionFormat') AS region,
    (payload -> 'applicationTimeMetrics'
             ->> 'cumulativeForegroundTime'
    )::INTERVAL AS cumulative_foreground_time,
    parse_byte_count(
      payload -> 'memoryMetrics'
             ->> 'peakMemoryUsage'
    ) AS peak_memory_usage_bytes
FROM metrics;
```

通过视图，你可以方便地像使用 schema 支持的关系型数据库一样，对所有指标 JSON payload 执行[聚合查询](https://www.postgresql.org/docs/current/functions-aggregate.html)：

```
SELECT avg(cumulative_foreground_time)
FROM key_performance_indicators;
--         avg
-- ══════════════════
--  @ 9 mins 41 secs

SELECT app_version, percentile_disc(0.5)
         WITHIN GROUP (ORDER BY peak_memory_usage_bytes)
         AS median
FROM key_performance_indicators
GROUP BY app_version;
--  app_version │  median
-- ═════════════╪═══════════
--  "1.0.1"     │ 192500000
--  "1.0.0"     │ 204800000
```

### 创建 Web 服务

在这个示例中，大部分繁重工作都委托给了 Postgres，使得服务器端的实现变得相当平淡。为完整起见，这里提供一些参考实现，分别使用 Ruby（Sinatra）和 JavaScript（Express）：

```
require 'sinatra/base'
require 'pg'
require 'sequel'

class App < Sinatra::Base
  configure do
    DB = Sequel.connect(ENV['DATABASE_URL'])
  end

  post '/collect' do
    DB[:metrics].insert(payload: request.body.read)
    status 204
  end
end
```

```
import express from 'express';
import { Pool } from 'pg';

const db = new Pool(
    connectionString: process.env.DATABASE_URL,
    ssl: process.env.NODE_ENV === 'production'
);

const app = express();
app.post('/collect', (request, response) => {
  db.query('INSERT INTO metrics (payload) VALUES ($1)', [request.body], (error, results) => {
    if (error) {
      throw error;
    }

    response.status(204);
  })
});

app.listen(process.env.PORT || 5000)
```

### 以 JSON 形式发送指标

现在我们已经设置好了一切，最后一步是实现所需的 `MXMetricManagerSubscriber` 委托方法 `didReceive(_:)`，将这些信息传递到我们的 Web 服务：

```
extension AppDelegate: MXMetricManagerSubscriber {
    func didReceive(_ payloads: [MXMetricPayload]) {
        for payload in payloads {
            let url = URL(string: "https://example.com/collect")!

            var request = URLRequest(url: url)
            request.httpMethod = "POST"
            request.httpBody = payload.jsonRepresentation()

            let task = URLSession.shared.dataTask(with: request)
            task.priority = URLSessionTask.lowPriority
            task.resume()
        }
    }
}
```

---

当你创造了一些东西并将其发布到世界上时，你就失去了与它的直接联系。这对于 App 和大学电台节目来说都是如此。如果没有用户研究或[侵入式广告技术](https://techcrunch.com/2019/02/06/iphone-session-replay-screenshots/)，事实是[我们很少知道人们是如何使用我们的软件的](https://xkcd.com/1172/)。

指标提供了一种便捷的方式，至少可以确保事情不会太慢或太耗电。尽管它们只能让我们从总体上大致了解人们如何享用我们的 App，但这已经足够帮助我们通过出色的用户体验来尊重我们的创作和我们的观众。
