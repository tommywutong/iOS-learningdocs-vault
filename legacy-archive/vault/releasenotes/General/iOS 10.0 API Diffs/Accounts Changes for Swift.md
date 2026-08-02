---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/Accounts.html
archived_at: '2026-07-18T02:55:06.252847Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# Accounts Changes for Swift

### Accounts

Modified [ACAccount](https://developer.apple.com/documentation/accounts/acaccount)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ACAccount : NSObject {     init!(accountType type: ACAccountType!)     var identifier: String! { get }     var accountType: ACAccountType!     var accountDescription: String!     var username: String!     var userFullName: String! { get }     var credential: ACAccountCredential! } ``` | -- |
| To | ``` class ACAccount : NSObject {     init!(accountType type: ACAccountType!)     weak var identifier: NSString! { get }     var accountType: ACAccountType!     var accountDescription: String!     var username: String!     var userFullName: String! { get }     var credential: ACAccountCredential!     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ACAccount : CVarArg { } extension ACAccount : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [ACAccount.identifier](https://developer.apple.com/documentation/accounts/acaccount/1543840-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! { get } ``` |
| To | ``` weak var identifier: NSString! { get } ``` |

Modified [ACAccountCredential](https://developer.apple.com/documentation/accounts/acaccountcredential)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ACAccountCredential : NSObject {     init!(OAuthToken token: String!, tokenSecret secret: String!)     init!(OAuth2Token token: String!, refreshToken refreshToken: String!, expiryDate expiryDate: NSDate!)     var oauthToken: String! } ``` | -- |
| To | ``` class ACAccountCredential : NSObject {     init!(oAuthToken token: String!, tokenSecret secret: String!)     init!(oAuth2Token token: String!, refreshToken refreshToken: String!, expiryDate expiryDate: Date!)     var oauthToken: String!     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ACAccountCredential : CVarArg { } extension ACAccountCredential : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [ACAccountCredential.init(oAuth2Token: String!, refreshToken: String!, expiryDate: Date!)](https://developer.apple.com/documentation/accounts/acaccountcredential/1507892-initwithoauth2token)

|  | Declaration |
| --- | --- |
| From | ``` init!(OAuth2Token token: String!, refreshToken refreshToken: String!, expiryDate expiryDate: NSDate!) ``` |
| To | ``` init!(oAuth2Token token: String!, refreshToken refreshToken: String!, expiryDate expiryDate: Date!) ``` |

Modified [ACAccountCredential.init(oAuthToken: String!, tokenSecret: String!)](https://developer.apple.com/documentation/accounts/acaccountcredential/1507896-initwithoauthtoken)

|  | Declaration |
| --- | --- |
| From | ``` init!(OAuthToken token: String!, tokenSecret secret: String!) ``` |
| To | ``` init!(oAuthToken token: String!, tokenSecret secret: String!) ``` |

Modified [ACAccountCredentialRenewResult [enum]](https://developer.apple.com/documentation/accounts/acaccountcredentialrenewresult)

|  | Declaration |
| --- | --- |
| From | ``` enum ACAccountCredentialRenewResult : Int {     case Renewed     case Rejected     case Failed } ``` |
| To | ``` enum ACAccountCredentialRenewResult : Int {     case renewed     case rejected     case failed } ``` |

Modified [ACAccountCredentialRenewResult.failed](https://developer.apple.com/documentation/accounts/acaccountcredentialrenewresult/acaccountcredentialrenewresultfailed)

|  | Declaration |
| --- | --- |
| From | ``` case Failed ``` |
| To | ``` case failed ``` |

Modified [ACAccountCredentialRenewResult.rejected](https://developer.apple.com/documentation/accounts/acaccountcredentialrenewresult/acaccountcredentialrenewresultrejected)

|  | Declaration |
| --- | --- |
| From | ``` case Rejected ``` |
| To | ``` case rejected ``` |

Modified [ACAccountCredentialRenewResult.renewed](https://developer.apple.com/documentation/accounts/acaccountcredentialrenewresult/renewed)

|  | Declaration |
| --- | --- |
| From | ``` case Renewed ``` |
| To | ``` case renewed ``` |

Modified [ACAccountStore](https://developer.apple.com/documentation/accounts/acaccountstore)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ACAccountStore : NSObject {     var accounts: [AnyObject]! { get }     func accountWithIdentifier(_ identifier: String!) -> ACAccount!     func accountTypeWithAccountTypeIdentifier(_ typeIdentifier: String!) -> ACAccountType!     func accountsWithAccountType(_ accountType: ACAccountType!) -> [AnyObject]!     func saveAccount(_ account: ACAccount!, withCompletionHandler completionHandler: ACAccountStoreSaveCompletionHandler!)     func requestAccessToAccountsWithType(_ accountType: ACAccountType!, withCompletionHandler handler: ACAccountStoreRequestAccessCompletionHandler!)     func requestAccessToAccountsWithType(_ accountType: ACAccountType!, options options: [NSObject : AnyObject]!, completion completion: ACAccountStoreRequestAccessCompletionHandler!)     func renewCredentialsForAccount(_ account: ACAccount!, completion completionHandler: ACAccountStoreCredentialRenewalHandler!)     func removeAccount(_ account: ACAccount!, withCompletionHandler completionHandler: ACAccountStoreRemoveCompletionHandler!) } ``` | -- |
| To | ``` class ACAccountStore : NSObject {     weak var accounts: NSArray! { get }     func account(withIdentifier identifier: String!) -> ACAccount!     func accountType(withAccountTypeIdentifier typeIdentifier: String!) -> ACAccountType!     func accounts(with accountType: ACAccountType!) -> [Any]!     func saveAccount(_ account: ACAccount!, withCompletionHandler completionHandler: Accounts.ACAccountStoreSaveCompletionHandler!)     func requestAccessToAccounts(with accountType: ACAccountType!, withCompletionHandler handler: Accounts.ACAccountStoreRequestAccessCompletionHandler!)     func requestAccessToAccounts(with accountType: ACAccountType!, options options: [AnyHashable : Any]! = [:], completion completion: Accounts.ACAccountStoreRequestAccessCompletionHandler!)     func renewCredentials(for account: ACAccount!, completion completionHandler: Accounts.ACAccountStoreCredentialRenewalHandler!)     func removeAccount(_ account: ACAccount!, withCompletionHandler completionHandler: Accounts.ACAccountStoreRemoveCompletionHandler!)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ACAccountStore : CVarArg { } extension ACAccountStore : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [ACAccountStore.account(withIdentifier: String!) -> ACAccount!](https://developer.apple.com/documentation/accounts/acaccountstore/1493947-accountwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func accountWithIdentifier(_ identifier: String!) -> ACAccount! ``` |
| To | ``` func account(withIdentifier identifier: String!) -> ACAccount! ``` |

Modified [ACAccountStore.accounts](https://developer.apple.com/documentation/accounts/acaccountstore/1493961-accounts)

|  | Declaration |
| --- | --- |
| From | ``` var accounts: [AnyObject]! { get } ``` |
| To | ``` weak var accounts: NSArray! { get } ``` |

Modified [ACAccountStore.accounts(with: ACAccountType!) -> [Any]!](https://developer.apple.com/documentation/accounts/acaccountstore/1493942-accountswithaccounttype)

|  | Declaration |
| --- | --- |
| From | ``` func accountsWithAccountType(_ accountType: ACAccountType!) -> [AnyObject]! ``` |
| To | ``` func accounts(with accountType: ACAccountType!) -> [Any]! ``` |

Modified [ACAccountStore.accountType(withAccountTypeIdentifier: String!) -> ACAccountType!](https://developer.apple.com/documentation/accounts/acaccountstore/1493967-accounttype)

|  | Declaration |
| --- | --- |
| From | ``` func accountTypeWithAccountTypeIdentifier(_ typeIdentifier: String!) -> ACAccountType! ``` |
| To | ``` func accountType(withAccountTypeIdentifier typeIdentifier: String!) -> ACAccountType! ``` |

Modified [ACAccountStore.removeAccount(_: ACAccount!, withCompletionHandler: Accounts.ACAccountStoreRemoveCompletionHandler!)](https://developer.apple.com/documentation/accounts/acaccountstore/1493968-removeaccount)

|  | Declaration |
| --- | --- |
| From | ``` func removeAccount(_ account: ACAccount!, withCompletionHandler completionHandler: ACAccountStoreRemoveCompletionHandler!) ``` |
| To | ``` func removeAccount(_ account: ACAccount!, withCompletionHandler completionHandler: Accounts.ACAccountStoreRemoveCompletionHandler!) ``` |

Modified [ACAccountStore.renewCredentials(for: ACAccount!, completion: Accounts.ACAccountStoreCredentialRenewalHandler!)](https://developer.apple.com/documentation/accounts/acaccountstore/1493959-renewcredentials)

|  | Declaration |
| --- | --- |
| From | ``` func renewCredentialsForAccount(_ account: ACAccount!, completion completionHandler: ACAccountStoreCredentialRenewalHandler!) ``` |
| To | ``` func renewCredentials(for account: ACAccount!, completion completionHandler: Accounts.ACAccountStoreCredentialRenewalHandler!) ``` |

Modified [ACAccountStore.requestAccessToAccounts(with: ACAccountType!, options: [AnyHashable : Any]!, completion: Accounts.ACAccountStoreRequestAccessCompletionHandler!)](https://developer.apple.com/documentation/accounts/acaccountstore/1493964-requestaccesstoaccounts)

|  | Declaration |
| --- | --- |
| From | ``` func requestAccessToAccountsWithType(_ accountType: ACAccountType!, options options: [NSObject : AnyObject]!, completion completion: ACAccountStoreRequestAccessCompletionHandler!) ``` |
| To | ``` func requestAccessToAccounts(with accountType: ACAccountType!, options options: [AnyHashable : Any]! = [:], completion completion: Accounts.ACAccountStoreRequestAccessCompletionHandler!) ``` |

Modified [ACAccountStore.saveAccount(_: ACAccount!, withCompletionHandler: Accounts.ACAccountStoreSaveCompletionHandler!)](https://developer.apple.com/documentation/accounts/acaccountstore/1493957-saveaccount)

|  | Declaration |
| --- | --- |
| From | ``` func saveAccount(_ account: ACAccount!, withCompletionHandler completionHandler: ACAccountStoreSaveCompletionHandler!) ``` |
| To | ``` func saveAccount(_ account: ACAccount!, withCompletionHandler completionHandler: Accounts.ACAccountStoreSaveCompletionHandler!) ``` |

Modified [ACAccountType](https://developer.apple.com/documentation/accounts/acaccounttype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ACAccountType : NSObject {     var accountTypeDescription: String! { get }     var identifier: String! { get }     var accessGranted: Bool { get } } ``` | -- |
| To | ``` class ACAccountType : NSObject {     var accountTypeDescription: String! { get }     var identifier: String! { get }     var accessGranted: Bool { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ACAccountType : CVarArg { } extension ACAccountType : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NSNotification.Name.ACAccountStoreDidChange](https://developer.apple.com/documentation/accounts/acaccountstoredidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | ACAccountStoreDidChangeNotification | ``` let ACAccountStoreDidChangeNotification: String ``` |
| To | ACAccountStoreDidChange | ``` static let ACAccountStoreDidChange: NSNotification.Name ``` |

Modified [ACAccountStoreCredentialRenewalHandler](https://developer.apple.com/documentation/accounts/acaccountstorecredentialrenewalhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias ACAccountStoreCredentialRenewalHandler = (ACAccountCredentialRenewResult, NSError!) -> Void ``` |
| To | ``` typealias ACAccountStoreCredentialRenewalHandler = (ACAccountCredentialRenewResult, Error?) -> Swift.Void ``` |

Modified [ACAccountStoreRemoveCompletionHandler](https://developer.apple.com/documentation/accounts/acaccountstoreremovecompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias ACAccountStoreRemoveCompletionHandler = (Bool, NSError!) -> Void ``` |
| To | ``` typealias ACAccountStoreRemoveCompletionHandler = (Bool, Error?) -> Swift.Void ``` |

Modified [ACAccountStoreRequestAccessCompletionHandler](https://developer.apple.com/documentation/accounts/acaccountstorerequestaccesscompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias ACAccountStoreRequestAccessCompletionHandler = (Bool, NSError!) -> Void ``` |
| To | ``` typealias ACAccountStoreRequestAccessCompletionHandler = (Bool, Error?) -> Swift.Void ``` |

Modified [ACAccountStoreSaveCompletionHandler](https://developer.apple.com/documentation/accounts/acaccountstoresavecompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias ACAccountStoreSaveCompletionHandler = (Bool, NSError!) -> Void ``` |
| To | ``` typealias ACAccountStoreSaveCompletionHandler = (Bool, Error?) -> Swift.Void ``` |

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
