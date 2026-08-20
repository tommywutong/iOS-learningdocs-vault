---
title: Using the correct Bluetooth LE Advertising and Connection Parameters for a
  stable connection
apple_id: DTS40017509
resource_type: QA
platform: tvOS|iOS|macOS
topic: Drivers, Kernel, & Hardware
technology: CoreBluetooth
published: '2017-09-26'
source_url: https://developer.apple.com/library/archive/qa/qa1931/_index.html
archived_at: '2026-07-18T02:37:10.691476Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1931

# Using the correct Bluetooth LE Advertising and Connection Parameters for a stable connection

## Q:  What advertising and connection parameters should I use in my Bluetooth LE accessory for a successful and stable connection with an Apple product?

A: Using incorrect advertising and connection parameters on a BLE accessory is a common source of issues, causing apps to not be able to discover, connect, or maintain a connection under real life conditions. In order to be able to establish and maintain a successful connection, you must follow not only the specifications prescribed by the Bluetooth SIG, but also the guidelines described in the [Bluetooth Accessory Design Guidelines for Apple Products](https://developer.apple.com/hardwaredrivers/BluetoothDesignGuidelines.pdf) document when designing and configuring your accessory.

You must follow the general advertising guidelines in the [Bluetooth Accessory Design Guidelines for Apple Products](https://developer.apple.com/hardwaredrivers/BluetoothDesignGuidelines.pdf) when constructing your advertising packets. A common mistake is to use improper advertising intervals, either due to misconfiguration or in order to save battery usage on the peripheral. Improper intervals are the most common reasons for your app to not be able to discover your accessory in the field, even though you may have observed discovery working properly in your tests.

The advertising interval of your peripheral affects the time to discovery and connect performance. Outside of ideal conditions, for example when your app is no longer active in the foreground, the time to discovery becomes longer. To maximize the probability of being discovered, the accessory must advertise at one of the listed intervals __exactly__.

The recommended advertising pattern and advertising intervals are:

- First, advertise at 20 ms intervals for at least 30 seconds
- If not discovered after 30 seconds, you may change to one of the following longer intervals: 152.5 ms, 211.25 ms, 318.75 ms, 417.5 ms, 546.25 ms, 760 ms, 852.5 ms, 1022.5 ms, 1285 ms

You must follow the general guidelines in the [Bluetooth Accessory Design Guidelines for Apple Products](https://developer.apple.com/hardwaredrivers/BluetoothDesignGuidelines.pdf) when establishing your connection parameters for your accessory. Common mistakes are to leave these values at their default values, or changing one or more of the parameters without considering the relationship between them.

There are certain rules and formulae that the parameters must follow. If the parameters do not comply with __all__ of these rules, the parameter request may be rejected, or the stability and the performance of the connection may be compromised.

- Interval Min ≥ 15 ms (multiples of 15 ms)
- Interval Min + 15 ms ≤ Interval Max (Interval Max == 15 ms is allowed)
- Interval Max \* (Slave Latency + 1) ≤ 2 seconds
- Interval Max \* (Slave Latency + 1) \* 3 < connSupervisionTimeout
- Slave Latency ≤ 30
- 2 seconds ≤ connSupervisionTimeout ≤ 6 seconds

Use the __BLE Parameter Validation Spreadsheet__ to check that your parameters are correct. Download link is at the end of this page.

- Download BLE Parameter Validation ("qa1931_BLE Parameter Validation.numbers.zip", 79.0K)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-09-26 | Updated the content and the spreadsheet calculations in accordance with the Bluetooth Accessory Design Guidelines for Apple Products (Release R8) |
| 2016-08-15 | New document that explains the importance of correct Bluetooth LE (BLE) connection parameters and demonstrates the formulae used to calculate correct values |

