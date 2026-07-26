---
title: PKRecurringPaymentSummaryItem
framework: PassKit (Apple Pay and Wallet)
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/passkit/pkrecurringpaymentsummaryitem
source_url: 'https://developer.apple.com/documentation/passkit/pkrecurringpaymentsummaryitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/passkit/pkrecurringpaymentsummaryitem.json'
content_hash: 'sha256:2c4bbe59ebb343ad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PassKit (Apple Pay and Wallet)](../passkit.md)

# PKRecurringPaymentSummaryItem

<sub>Class</sub>

An object that defines a summary item for a payment that occurs repeatedly at a specified interval, such as a subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class PKRecurringPaymentSummaryItem
```

## Overview

[PKRecurringPaymentSummaryItem](pkrecurringpaymentsummaryitem.md) is a subclass of [PKPaymentSummaryItemType](pkpaymentsummaryitemtype.md) and inherits all properties of the parent class.

Add a summary item of this type to the [paymentSummaryItems](pkpaymentrequest/paymentsummaryitems.md) property of a [PKPaymentRequest](pkpaymentrequest.md) to display to the user a recurring payment in the summary items on the payment sheet.

To describe a recurring payment, set the summary item values as follows:

- In the [amount](pkpaymentsummaryitem/amount.md) property, provide the billing amount for the set interval, for example, the amount charged per week if the [intervalUnit](pkrecurringpaymentsummaryitem/intervalunit.md) is a week.
- Omit the [type](pkpaymentsummaryitem/type.md) property. The summary item type is only relevant for the [PKPaymentSummaryItem](pkpaymentsummaryitem.md) parent class.
- Set the [startDate](pkrecurringpaymentsummaryitem/startdate.md) and [endDate](pkrecurringpaymentsummaryitem/enddate.md) to represent the term for the recurring payments, as appropriate.
- Set the [intervalUnit](pkrecurringpaymentsummaryitem/intervalunit.md), [intervalCount](pkrecurringpaymentsummaryitem/intervalcount.md), and [endDate](pkrecurringpaymentsummaryitem/enddate.md) to specify a number of repeating payments.

For example, the following code shows a summary item that specifies six monthly payments that start on the transaction date:

```swift
let recurringPayment = PKRecurringPaymentSummaryItem(label: "Total Payment",                                                  NSDecimalNumber(string: "199.99"))

// Payment starts today.
recurringPayment.startDate = nil

// Pay once a month.
recurringPayment.intervalUnit = .month
recurringPayment.intervalCount = 1

// Make 5 more payments for a total of 6 payments.
var dateComponent = DateComponents()
dateComponent.month = 5
recurringPayment.endDate = Calendar.current.date(byAdding: dateComponent, Date())
```

The payment interval is a combination of the [intervalUnit](pkrecurringpaymentsummaryitem/intervalunit.md) and the [intervalCount](pkrecurringpaymentsummaryitem/intervalcount.md). For example, if you set the [intervalUnit](pkrecurringpaymentsummaryitem/intervalunit.md) to .[month](../corefoundation/cfcalendarunit/month.md) and [intervalCount](pkrecurringpaymentsummaryitem/intervalcount.md) to `3`, then the payment interval is three months.

## Relationships

- **Inherits From**: [PKPaymentSummaryItem](pkpaymentsummaryitem.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Setting the payment period

- [startDate](pkrecurringpaymentsummaryitem/startdate.md) — The date of the first payment.
- [endDate](pkrecurringpaymentsummaryitem/enddate.md) — The date of the final payment.

### Setting the payment interval

- [intervalUnit](pkrecurringpaymentsummaryitem/intervalunit.md) — The amount of time – in calendar units such as day, month, or year – that represents a fraction of the total payment interval.
- [intervalCount](pkrecurringpaymentsummaryitem/intervalcount.md) — The number of interval units that make up the total payment interval.

## See Also

### Setting the payment summary items

- [paymentSummaryItems](pkpaymentrequest/paymentsummaryitems.md) — An array of payment summary item objects that summarize the amount of the payment.
- [PKPaymentSummaryItem](pkpaymentsummaryitem.md) — An object that defines a summary item in a payment request, taxes, discounts, shipping, a grand total, and the like.
- [PKDeferredPaymentSummaryItem](pkdeferredpaymentsummaryitem.md) — An object that defines a summary item for a payment that occurs at a later date, such as a pre-order.
