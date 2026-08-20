---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/StoreKit.html
archived_at: '2026-07-18T02:53:44.422335Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# StoreKit Changes for Swift

### StoreKit

Removed SKDownloadState.valueAdded [SKDownload.transaction](https://developer.apple.com/documentation/storekit/skdownload/1458949-transaction)Added SKDownloadState.init(rawValue: Int)Added SKDownloadState.rawValueModified [SKDownload](https://developer.apple.com/documentation/storekit/skdownload)

|  | Declaration |
| --- | --- |
| From | ``` class SKDownload : NSObject {     var contentIdentifier: String! { get }     var state: SKDownloadState { get }     @NSCopying var contentURL: NSURL! { get }     var progress: Float { get }     @NSCopying var error: NSError! { get }     var timeRemaining: NSTimeInterval { get }     @NSCopying var contentLength: NSNumber! { get }     var contentVersion: String! { get }     class func contentURLForProductID(_ productID: String!) -> NSURL!     class func deleteContentForProductID(_ productID: String!) } ``` |
| To | ``` class SKDownload : NSObject {     var contentIdentifier: String { get }     var state: SKDownloadState { get }     @NSCopying var contentURL: NSURL? { get }     var progress: Float { get }     @NSCopying var error: NSError? { get }     var timeRemaining: NSTimeInterval { get }     @NSCopying var contentLength: NSNumber { get }     var contentVersion: String? { get }     var transaction: SKPaymentTransaction? { get }     class func contentURLForProductID(_ productID: String) -> NSURL?     class func deleteContentForProductID(_ productID: String) } ``` |

Modified [SKDownload.contentIdentifier](https://developer.apple.com/documentation/storekit/skdownload/1458941-contentidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var contentIdentifier: String! { get } ``` |
| To | ``` var contentIdentifier: String { get } ``` |

Modified [SKDownload.contentLength](https://developer.apple.com/documentation/storekit/skdownload/1458932-contentlength)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var contentLength: NSNumber! { get } ``` |
| To | ``` @NSCopying var contentLength: NSNumber { get } ``` |

Modified [SKDownload.contentURL](https://developer.apple.com/documentation/storekit/skdownload/1458930-contenturl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var contentURL: NSURL! { get } ``` |
| To | ``` @NSCopying var contentURL: NSURL? { get } ``` |

Modified [SKDownload.contentURLForProductID(_: String) -> NSURL? [class]](https://developer.apple.com/documentation/storekit/skdownload/1458924-contenturlforproductid)

|  | Declaration |
| --- | --- |
| From | ``` class func contentURLForProductID(_ productID: String!) -> NSURL! ``` |
| To | ``` class func contentURLForProductID(_ productID: String) -> NSURL? ``` |

Modified [SKDownload.contentVersion](https://developer.apple.com/documentation/storekit/skdownload/1458916-contentversion)

|  | Declaration |
| --- | --- |
| From | ``` var contentVersion: String! { get } ``` |
| To | ``` var contentVersion: String? { get } ``` |

Modified [SKDownload.deleteContentForProductID(_: String) [class]](https://developer.apple.com/documentation/storekit/skdownload/1458926-deletecontentforproductid)

|  | Declaration |
| --- | --- |
| From | ``` class func deleteContentForProductID(_ productID: String!) ``` |
| To | ``` class func deleteContentForProductID(_ productID: String) ``` |

Modified [SKDownload.error](https://developer.apple.com/documentation/storekit/skdownload/1458914-error)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var error: NSError! { get } ``` |
| To | ``` @NSCopying var error: NSError? { get } ``` |

Modified [SKDownloadState [struct]](https://developer.apple.com/documentation/storekit/skdownloadstate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SKDownloadState {     init(_ value: Int)     var value: Int } ``` | -- |
| To | ``` struct SKDownloadState : RawRepresentable {     init(_ rawValue: Int)     init(rawValue rawValue: Int)     var rawValue: Int } ``` | RawRepresentable |

Modified [SKMutablePayment](https://developer.apple.com/documentation/storekit/skmutablepayment)

|  | Declaration |
| --- | --- |
| From | ``` class SKMutablePayment : SKPayment {     var productIdentifier: String!     var quantity: Int     @NSCopying var requestData: NSData!     var applicationUsername: String! } ``` |
| To | ``` class SKMutablePayment : SKPayment {     var productIdentifier: String     var quantity: Int     @NSCopying var requestData: NSData?     var applicationUsername: String? } ``` |

Modified [SKMutablePayment.applicationUsername](https://developer.apple.com/documentation/storekit/skmutablepayment/1506088-applicationusername)

|  | Declaration |
| --- | --- |
| From | ``` var applicationUsername: String! ``` |
| To | ``` var applicationUsername: String? ``` |

Modified [SKMutablePayment.productIdentifier](https://developer.apple.com/documentation/storekit/skmutablepayment/1505983-productidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var productIdentifier: String! ``` |
| To | ``` var productIdentifier: String ``` |

Modified [SKMutablePayment.requestData](https://developer.apple.com/documentation/storekit/skmutablepayment/1505974-requestdata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var requestData: NSData! ``` |
| To | ``` @NSCopying var requestData: NSData? ``` |

Modified [SKPayment](https://developer.apple.com/documentation/storekit/skpayment)

|  | Declaration |
| --- | --- |
| From | ``` class SKPayment : NSObject, NSCopying, NSMutableCopying {     class func paymentWithProduct(_ product: SKProduct!) -> AnyObject!     var productIdentifier: String! { get }     @NSCopying var requestData: NSData! { get }     var quantity: Int { get }     var applicationUsername: String! { get } } ``` |
| To | ``` class SKPayment : NSObject, NSCopying, NSMutableCopying {     class func paymentWithProduct(_ product: SKProduct) -> AnyObject     var productIdentifier: String { get }     @NSCopying var requestData: NSData? { get }     var quantity: Int { get }     var applicationUsername: String? { get } } ``` |

Modified [SKPayment.applicationUsername](https://developer.apple.com/documentation/storekit/skpayment/1506116-applicationusername)

|  | Declaration |
| --- | --- |
| From | ``` var applicationUsername: String! { get } ``` |
| To | ``` var applicationUsername: String? { get } ``` |

Modified [SKPayment.paymentWithProduct(_: SKProduct) -> AnyObject [class]](https://developer.apple.com/documentation/storekit/skpayment/1506008-init)

|  | Declaration |
| --- | --- |
| From | ``` class func paymentWithProduct(_ product: SKProduct!) -> AnyObject! ``` |
| To | ``` class func paymentWithProduct(_ product: SKProduct) -> AnyObject ``` |

Modified [SKPayment.productIdentifier](https://developer.apple.com/documentation/storekit/skpayment/1506155-productidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var productIdentifier: String! { get } ``` |
| To | ``` var productIdentifier: String { get } ``` |

Modified [SKPayment.requestData](https://developer.apple.com/documentation/storekit/skpayment/1506159-requestdata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var requestData: NSData! { get } ``` |
| To | ``` @NSCopying var requestData: NSData? { get } ``` |

Modified [SKPaymentQueue](https://developer.apple.com/documentation/storekit/skpaymentqueue)

|  | Declaration |
| --- | --- |
| From | ``` class SKPaymentQueue : NSObject {     class func defaultQueue() -> SKPaymentQueue!     class func canMakePayments() -> Bool     func addPayment(_ payment: SKPayment!)     func restoreCompletedTransactions()     func restoreCompletedTransactionsWithApplicationUsername(_ username: String!)     func finishTransaction(_ transaction: SKPaymentTransaction!)     func addTransactionObserver(_ observer: SKPaymentTransactionObserver!)     func removeTransactionObserver(_ observer: SKPaymentTransactionObserver!)     var transactions: [AnyObject]! { get }     func startDownloads(_ downloads: [AnyObject]!)     func pauseDownloads(_ downloads: [AnyObject]!)     func resumeDownloads(_ downloads: [AnyObject]!)     func cancelDownloads(_ downloads: [AnyObject]!) } ``` |
| To | ``` class SKPaymentQueue : NSObject {     class func defaultQueue() -> SKPaymentQueue     class func canMakePayments() -> Bool     func addPayment(_ payment: SKPayment)     func restoreCompletedTransactions()     func restoreCompletedTransactionsWithApplicationUsername(_ username: String?)     func finishTransaction(_ transaction: SKPaymentTransaction)     func addTransactionObserver(_ observer: SKPaymentTransactionObserver)     func removeTransactionObserver(_ observer: SKPaymentTransactionObserver)     var transactions: [SKPaymentTransaction]? { get }     func startDownloads(_ downloads: [SKDownload])     func pauseDownloads(_ downloads: [SKDownload])     func resumeDownloads(_ downloads: [SKDownload])     func cancelDownloads(_ downloads: [SKDownload]) } ``` |

Modified [SKPaymentQueue.addPayment(_: SKPayment)](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506036-addpayment)

|  | Declaration |
| --- | --- |
| From | ``` func addPayment(_ payment: SKPayment!) ``` |
| To | ``` func addPayment(_ payment: SKPayment) ``` |

Modified [SKPaymentQueue.addTransactionObserver(_: SKPaymentTransactionObserver)](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506042-addtransactionobserver)

|  | Declaration |
| --- | --- |
| From | ``` func addTransactionObserver(_ observer: SKPaymentTransactionObserver!) ``` |
| To | ``` func addTransactionObserver(_ observer: SKPaymentTransactionObserver) ``` |

Modified [SKPaymentQueue.cancelDownloads(_: [SKDownload])](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506092-canceldownloads)

|  | Declaration |
| --- | --- |
| From | ``` func cancelDownloads(_ downloads: [AnyObject]!) ``` |
| To | ``` func cancelDownloads(_ downloads: [SKDownload]) ``` |

Modified [SKPaymentQueue.defaultQueue() -> SKPaymentQueue [class]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505990-default)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultQueue() -> SKPaymentQueue! ``` |
| To | ``` class func defaultQueue() -> SKPaymentQueue ``` |

Modified [SKPaymentQueue.finishTransaction(_: SKPaymentTransaction)](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506003-finishtransaction)

|  | Declaration |
| --- | --- |
| From | ``` func finishTransaction(_ transaction: SKPaymentTransaction!) ``` |
| To | ``` func finishTransaction(_ transaction: SKPaymentTransaction) ``` |

Modified [SKPaymentQueue.pauseDownloads(_: [SKDownload])](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506053-pausedownloads)

|  | Declaration |
| --- | --- |
| From | ``` func pauseDownloads(_ downloads: [AnyObject]!) ``` |
| To | ``` func pauseDownloads(_ downloads: [SKDownload]) ``` |

Modified [SKPaymentQueue.removeTransactionObserver(_: SKPaymentTransactionObserver)](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506165-remove)

|  | Declaration |
| --- | --- |
| From | ``` func removeTransactionObserver(_ observer: SKPaymentTransactionObserver!) ``` |
| To | ``` func removeTransactionObserver(_ observer: SKPaymentTransactionObserver) ``` |

Modified [SKPaymentQueue.restoreCompletedTransactionsWithApplicationUsername(_: String?)](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505992-restorecompletedtransactions)

|  | Declaration |
| --- | --- |
| From | ``` func restoreCompletedTransactionsWithApplicationUsername(_ username: String!) ``` |
| To | ``` func restoreCompletedTransactionsWithApplicationUsername(_ username: String?) ``` |

Modified [SKPaymentQueue.resumeDownloads(_: [SKDownload])](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506096-resume)

|  | Declaration |
| --- | --- |
| From | ``` func resumeDownloads(_ downloads: [AnyObject]!) ``` |
| To | ``` func resumeDownloads(_ downloads: [SKDownload]) ``` |

Modified [SKPaymentQueue.startDownloads(_: [SKDownload])](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505998-startdownloads)

|  | Declaration |
| --- | --- |
| From | ``` func startDownloads(_ downloads: [AnyObject]!) ``` |
| To | ``` func startDownloads(_ downloads: [SKDownload]) ``` |

Modified [SKPaymentQueue.transactions](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506026-transactions)

|  | Declaration |
| --- | --- |
| From | ``` var transactions: [AnyObject]! { get } ``` |
| To | ``` var transactions: [SKPaymentTransaction]? { get } ``` |

Modified [SKPaymentTransaction](https://developer.apple.com/documentation/storekit/skpaymenttransaction)

|  | Declaration |
| --- | --- |
| From | ``` class SKPaymentTransaction : NSObject {     var error: NSError! { get }     var originalTransaction: SKPaymentTransaction! { get }     var payment: SKPayment! { get }     var transactionDate: NSDate! { get }     var transactionIdentifier: String! { get }     var downloads: [AnyObject]! { get }     var transactionState: SKPaymentTransactionState { get } } ``` |
| To | ``` class SKPaymentTransaction : NSObject {     var error: NSError? { get }     var originalTransaction: SKPaymentTransaction? { get }     var payment: SKPayment { get }     var transactionDate: NSDate? { get }     var transactionIdentifier: String? { get }     var downloads: [AnyObject]? { get }     var transactionState: SKPaymentTransactionState { get } } ``` |

Modified [SKPaymentTransaction.downloads](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411282-downloads)

|  | Declaration |
| --- | --- |
| From | ``` var downloads: [AnyObject]! { get } ``` |
| To | ``` var downloads: [AnyObject]? { get } ``` |

Modified [SKPaymentTransaction.error](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411269-error)

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError! { get } ``` |
| To | ``` var error: NSError? { get } ``` |

Modified [SKPaymentTransaction.originalTransaction](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411284-originaltransaction)

|  | Declaration |
| --- | --- |
| From | ``` var originalTransaction: SKPaymentTransaction! { get } ``` |
| To | ``` var originalTransaction: SKPaymentTransaction? { get } ``` |

Modified [SKPaymentTransaction.payment](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411286-payment)

|  | Declaration |
| --- | --- |
| From | ``` var payment: SKPayment! { get } ``` |
| To | ``` var payment: SKPayment { get } ``` |

Modified [SKPaymentTransaction.transactionDate](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411273-transactiondate)

|  | Declaration |
| --- | --- |
| From | ``` var transactionDate: NSDate! { get } ``` |
| To | ``` var transactionDate: NSDate? { get } ``` |

Modified [SKPaymentTransaction.transactionIdentifier](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411288-transactionidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var transactionIdentifier: String! { get } ``` |
| To | ``` var transactionIdentifier: String? { get } ``` |

Modified [SKPaymentTransactionObserver](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver)

|  | Declaration |
| --- | --- |
| From | ``` protocol SKPaymentTransactionObserver : NSObjectProtocol {     func paymentQueue(_ queue: SKPaymentQueue!, updatedTransactions transactions: [AnyObject]!)     optional func paymentQueue(_ queue: SKPaymentQueue!, removedTransactions transactions: [AnyObject]!)     optional func paymentQueue(_ queue: SKPaymentQueue!, restoreCompletedTransactionsFailedWithError error: NSError!)     optional func paymentQueueRestoreCompletedTransactionsFinished(_ queue: SKPaymentQueue!)     optional func paymentQueue(_ queue: SKPaymentQueue!, updatedDownloads downloads: [AnyObject]!) } ``` |
| To | ``` protocol SKPaymentTransactionObserver : NSObjectProtocol {     func paymentQueue(_ queue: SKPaymentQueue, updatedTransactions transactions: [SKPaymentTransaction])     optional func paymentQueue(_ queue: SKPaymentQueue, removedTransactions transactions: [SKPaymentTransaction])     optional func paymentQueue(_ queue: SKPaymentQueue, restoreCompletedTransactionsFailedWithError error: NSError)     optional func paymentQueueRestoreCompletedTransactionsFinished(_ queue: SKPaymentQueue)     optional func paymentQueue(_ queue: SKPaymentQueue, updatedDownloads downloads: [SKDownload]) } ``` |

Modified [SKPaymentTransactionObserver.paymentQueue(_: SKPaymentQueue, removedTransactions: [SKPaymentTransaction])](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1505994-paymentqueue)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func paymentQueue(_ queue: SKPaymentQueue!, removedTransactions transactions: [AnyObject]!) ``` | OS X 10.10 |
| To | ``` optional func paymentQueue(_ queue: SKPaymentQueue, removedTransactions transactions: [SKPaymentTransaction]) ``` | OS X 10.7 |

Modified [SKPaymentTransactionObserver.paymentQueue(_: SKPaymentQueue, restoreCompletedTransactionsFailedWithError: NSError)](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1506063-paymentqueue)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func paymentQueue(_ queue: SKPaymentQueue!, restoreCompletedTransactionsFailedWithError error: NSError!) ``` | OS X 10.10 |
| To | ``` optional func paymentQueue(_ queue: SKPaymentQueue, restoreCompletedTransactionsFailedWithError error: NSError) ``` | OS X 10.7 |

Modified [SKPaymentTransactionObserver.paymentQueue(_: SKPaymentQueue, updatedDownloads: [SKDownload])](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1506073-paymentqueue)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func paymentQueue(_ queue: SKPaymentQueue!, updatedDownloads downloads: [AnyObject]!) ``` | OS X 10.10 |
| To | ``` optional func paymentQueue(_ queue: SKPaymentQueue, updatedDownloads downloads: [SKDownload]) ``` | OS X 10.8 |

Modified [SKPaymentTransactionObserver.paymentQueue(_: SKPaymentQueue, updatedTransactions: [SKPaymentTransaction])](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1506107-paymentqueue)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func paymentQueue(_ queue: SKPaymentQueue!, updatedTransactions transactions: [AnyObject]!) ``` | OS X 10.10 |
| To | ``` func paymentQueue(_ queue: SKPaymentQueue, updatedTransactions transactions: [SKPaymentTransaction]) ``` | OS X 10.7 |

Modified [SKPaymentTransactionObserver.paymentQueueRestoreCompletedTransactionsFinished(_: SKPaymentQueue)](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1506101-paymentqueuerestorecompletedtran)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func paymentQueueRestoreCompletedTransactionsFinished(_ queue: SKPaymentQueue!) ``` | OS X 10.10 |
| To | ``` optional func paymentQueueRestoreCompletedTransactionsFinished(_ queue: SKPaymentQueue) ``` | OS X 10.7 |

Modified [SKProduct](https://developer.apple.com/documentation/storekit/skproduct)

|  | Declaration |
| --- | --- |
| From | ``` class SKProduct : NSObject {     var localizedDescription: String! { get }     var localizedTitle: String! { get }     var price: NSDecimalNumber! { get }     var priceLocale: NSLocale! { get }     var productIdentifier: String! { get }     var downloadable: Bool { get }     var contentVersion: String! { get }     var contentLengths: [AnyObject]! { get } } ``` |
| To | ``` class SKProduct : NSObject {     var localizedDescription: String? { get }     var localizedTitle: String? { get }     var price: NSDecimalNumber? { get }     var priceLocale: NSLocale? { get }     var productIdentifier: String? { get }     var downloadable: Bool { get }     var contentVersion: String? { get }     var contentLengths: [NSNumber]? { get } } ``` |

Modified [SKProduct.contentLengths](https://developer.apple.com/documentation/storekit/skproduct/1506157-contentlengths)

|  | Declaration |
| --- | --- |
| From | ``` var contentLengths: [AnyObject]! { get } ``` |
| To | ``` var contentLengths: [NSNumber]? { get } ``` |

Modified [SKProduct.contentVersion](https://developer.apple.com/documentation/storekit/skproduct/1505996-contentversion)

|  | Declaration |
| --- | --- |
| From | ``` var contentVersion: String! { get } ``` |
| To | ``` var contentVersion: String? { get } ``` |

Modified [SKProduct.localizedDescription](https://developer.apple.com/documentation/storekit/skproduct/1506040-localizeddescription)

|  | Declaration |
| --- | --- |
| From | ``` var localizedDescription: String! { get } ``` |
| To | ``` var localizedDescription: String? { get } ``` |

Modified [SKProduct.localizedTitle](https://developer.apple.com/documentation/storekit/skproduct/1506001-localizedtitle)

|  | Declaration |
| --- | --- |
| From | ``` var localizedTitle: String! { get } ``` |
| To | ``` var localizedTitle: String? { get } ``` |

Modified [SKProduct.price](https://developer.apple.com/documentation/storekit/skproduct/1506094-price)

|  | Declaration |
| --- | --- |
| From | ``` var price: NSDecimalNumber! { get } ``` |
| To | ``` var price: NSDecimalNumber? { get } ``` |

Modified [SKProduct.priceLocale](https://developer.apple.com/documentation/storekit/skproduct/1506145-pricelocale)

|  | Declaration |
| --- | --- |
| From | ``` var priceLocale: NSLocale! { get } ``` |
| To | ``` var priceLocale: NSLocale? { get } ``` |

Modified [SKProduct.productIdentifier](https://developer.apple.com/documentation/storekit/skproduct/1506080-productidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var productIdentifier: String! { get } ``` |
| To | ``` var productIdentifier: String? { get } ``` |

Modified [SKProductsRequest](https://developer.apple.com/documentation/storekit/skproductsrequest)

|  | Declaration |
| --- | --- |
| From | ``` class SKProductsRequest : SKRequest {     init!(productIdentifiers productIdentifiers: Set<NSObject>!)     unowned(unsafe) var delegate: SKProductsRequestDelegate! } ``` |
| To | ``` class SKProductsRequest : SKRequest {     init(productIdentifiers productIdentifiers: Set<NSObject>)     unowned(unsafe) var delegate: SKProductsRequestDelegate? } ``` |

Modified [SKProductsRequest.delegate](https://developer.apple.com/documentation/storekit/skproductsrequest/1506142-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: SKProductsRequestDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: SKProductsRequestDelegate? ``` |

Modified [SKProductsRequest.init(productIdentifiers: Set<NSObject>)](https://developer.apple.com/documentation/storekit/skproductsrequest/1506172-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(productIdentifiers productIdentifiers: Set<NSObject>!) ``` |
| To | ``` init(productIdentifiers productIdentifiers: Set<NSObject>) ``` |

Modified [SKProductsRequestDelegate](https://developer.apple.com/documentation/storekit/skproductsrequestdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol SKProductsRequestDelegate : SKRequestDelegate, NSObjectProtocol {     func productsRequest(_ request: SKProductsRequest!, didReceiveResponse response: SKProductsResponse!) } ``` |
| To | ``` protocol SKProductsRequestDelegate : SKRequestDelegate, NSObjectProtocol {     func productsRequest(_ request: SKProductsRequest, didReceiveResponse response: SKProductsResponse) } ``` |

Modified [SKProductsRequestDelegate.productsRequest(_: SKProductsRequest, didReceiveResponse: SKProductsResponse)](https://developer.apple.com/documentation/storekit/skproductsrequestdelegate/1506070-productsrequest)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func productsRequest(_ request: SKProductsRequest!, didReceiveResponse response: SKProductsResponse!) ``` | OS X 10.10 |
| To | ``` func productsRequest(_ request: SKProductsRequest, didReceiveResponse response: SKProductsResponse) ``` | OS X 10.7 |

Modified [SKProductsResponse](https://developer.apple.com/documentation/storekit/skproductsresponse)

|  | Declaration |
| --- | --- |
| From | ``` class SKProductsResponse : NSObject {     var products: [AnyObject]! { get }     var invalidProductIdentifiers: [AnyObject]! { get } } ``` |
| To | ``` class SKProductsResponse : NSObject {     var products: [SKProduct]? { get }     var invalidProductIdentifiers: [String]? { get } } ``` |

Modified [SKProductsResponse.invalidProductIdentifiers](https://developer.apple.com/documentation/storekit/skproductsresponse/1505985-invalidproductidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` var invalidProductIdentifiers: [AnyObject]! { get } ``` |
| To | ``` var invalidProductIdentifiers: [String]? { get } ``` |

Modified [SKProductsResponse.products](https://developer.apple.com/documentation/storekit/skproductsresponse/1506047-products)

|  | Declaration |
| --- | --- |
| From | ``` var products: [AnyObject]! { get } ``` |
| To | ``` var products: [SKProduct]? { get } ``` |

Modified [SKReceiptRefreshRequest](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest)

|  | Declaration |
| --- | --- |
| From | ``` class SKReceiptRefreshRequest : SKRequest {     init!(receiptProperties properties: [NSObject : AnyObject]!)     var receiptProperties: [NSObject : AnyObject]! { get } } ``` |
| To | ``` class SKReceiptRefreshRequest : SKRequest {     init?(receiptProperties properties: [String : AnyObject])     var receiptProperties: [String : AnyObject]? { get } } ``` |

Modified [SKReceiptRefreshRequest.init(receiptProperties: [String : AnyObject])](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/1506038-initwithreceiptproperties)

|  | Declaration |
| --- | --- |
| From | ``` init!(receiptProperties properties: [NSObject : AnyObject]!) ``` |
| To | ``` init?(receiptProperties properties: [String : AnyObject]) ``` |

Modified [SKReceiptRefreshRequest.receiptProperties](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/1506029-receiptproperties)

|  | Declaration |
| --- | --- |
| From | ``` var receiptProperties: [NSObject : AnyObject]! { get } ``` |
| To | ``` var receiptProperties: [String : AnyObject]? { get } ``` |

Modified [SKRequest](https://developer.apple.com/documentation/storekit/skrequest)

|  | Declaration |
| --- | --- |
| From | ``` class SKRequest : NSObject {     unowned(unsafe) var delegate: SKRequestDelegate!     func cancel()     func start() } ``` |
| To | ``` class SKRequest : NSObject {     unowned(unsafe) var delegate: SKRequestDelegate?     func cancel()     func start() } ``` |

Modified [SKRequest.delegate](https://developer.apple.com/documentation/storekit/skrequest/1385530-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: SKRequestDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: SKRequestDelegate? ``` |

Modified [SKRequestDelegate](https://developer.apple.com/documentation/storekit/skrequestdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol SKRequestDelegate : NSObjectProtocol {     optional func requestDidFinish(_ request: SKRequest!)     optional func request(_ request: SKRequest!, didFailWithError error: NSError!) } ``` |
| To | ``` protocol SKRequestDelegate : NSObjectProtocol {     optional func requestDidFinish(_ request: SKRequest)     optional func request(_ request: SKRequest, didFailWithError error: NSError?) } ``` |

Modified [SKRequestDelegate.request(_: SKRequest, didFailWithError: NSError?)](https://developer.apple.com/documentation/storekit/skrequestdelegate/1385536-request)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func request(_ request: SKRequest!, didFailWithError error: NSError!) ``` | OS X 10.10 |
| To | ``` optional func request(_ request: SKRequest, didFailWithError error: NSError?) ``` | OS X 10.7 |

Modified [SKRequestDelegate.requestDidFinish(_: SKRequest)](https://developer.apple.com/documentation/storekit/skrequestdelegate/1385532-requestdidfinish)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func requestDidFinish(_ request: SKRequest!) ``` | OS X 10.10 |
| To | ``` optional func requestDidFinish(_ request: SKRequest) ``` | OS X 10.7 |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
