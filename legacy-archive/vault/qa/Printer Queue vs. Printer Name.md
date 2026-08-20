---
title: Printer Queue vs. Printer Name
apple_id: DTS10003488
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2007-04-26'
source_url: https://developer.apple.com/library/archive/qa/qa1407/_index.html
archived_at: '2026-07-18T02:30:31.844868Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1407

# Printer Queue vs. Printer Name

## Q:  What is the difference between the Printer Name that is visible in the print dialog and the name of a Printer Queue?

A: What is the difference between the Printer Name that is visible in the print dialog and the name of a Printer Queue?

The printer name is the user's chosen name for a print queue, and is displayed by the Print & Faxes Preferences Pane and in Print Dialogs. This name should always be presented to the user when referencing a printer queue. There are no guarantees of uniqueness among printer names.

The name of a Printer Queue is a unique internal representation that specifies that specific print queue. This name is also known as, and hereafter referred to as, the Printer ID. It is a unique name that can always be used to reference a specific print queue. No matter how many print queues the user creates the Printer IDs created will always be unique.

To reliably reference a particular print queue, and therefore a specific printer, it is necessary to always use a Printer ID. You can reference a printer by Printer ID by creating a `PMPrinter` using `PMPrinterCreateFromPrinterID`. The `PMPrinter` data type neatly wraps Printer Name or Printer ID into a single package, allowing easy access to either.

Typically you do not need to know the Printer ID to print. However in some limited situations it makes sense to save the selected printer and automatically use it when needed (for example to print receipts for a point-of-sale application). The Printer ID provides the necessary persistent reference, since you cannot save a `PMPrinter` to your preferences. So using a Printer ID you can save a reference to a print queue that is valid for the life of that print queue.

The `PMPrinter` data structure is used to keep track of Printer Queues by Mac OS X. It allows easy access to both the Printer ID and Printer Name of the associated queue via `PMPrinterGetID` & `PMPrinterGetName`. `PMPrinterCreateFromPrinterID` allows you to convert a Printer ID into a `PMPrinter`. Finally `PMSessionGetCurrentPrinter` allows you to get the current `PMPrinter` from a `PMPrintSession`, while `PMSessionSetCurrentPMPrinter` allows you to set the current `PMPrinter`.

For an example of using these APIs to save and restore printer settings, visit [Technical Note TN2155: Saving Printer Settings for Automatic Printing](https://developer.apple.com/technotes/tn2007/tn2155.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-04-26 | Updated for Mac OS X 10.4 and to reference TN2155. |
| 2005-01-27 | New document that explains the difference between a printer queue and a printer name. |

