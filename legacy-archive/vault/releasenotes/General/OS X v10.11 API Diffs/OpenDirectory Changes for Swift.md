---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/OpenDirectory.html
archived_at: '2026-07-18T02:53:40.466786Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# OpenDirectory Changes for Swift

### OpenDirectory

Removed ODFrameworkErrors.valueAdded ODFrameworkErrors.init(rawValue: UInt32)Added ODFrameworkErrors.rawValueAdded [kODPolicyKeyContentDescription](https://developer.apple.com/documentation/opendirectory/kodpolicykeycontentdescription)Added [kODPolicyKeyEvaluationDetails](https://developer.apple.com/documentation/opendirectory/kodpolicykeyevaluationdetails)Added [kODPolicyKeyPolicySatisfied](https://developer.apple.com/documentation/opendirectory/kodpolicykeypolicysatisfied)Modified [ODConfiguration](https://developer.apple.com/documentation/opendirectory/odconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` class ODConfiguration : NSObject {     var nodeName: String!     var comment: String!     var defaultMappings: ODMappings!     var templateName: String!     var virtualSubnodes: [AnyObject]!     var hideRegistration: Bool     var preferredDestinationHostName: String!     var preferredDestinationHostPort: UInt16     var trustAccount: String! { get }     var trustMetaAccount: String! { get }     var trustKerberosPrincipal: String! { get }     var trustType: String! { get }     var trustUsesMutualAuthentication: Bool { get }     var trustUsesKerberosKeytab: Bool { get }     var trustUsesSystemKeychain: Bool { get }     var packetSigning: Int     var packetEncryption: Int     var manInTheMiddleProtection: Bool     var queryTimeoutInSeconds: Int     var connectionSetupTimeoutInSeconds: Int     var connectionIdleTimeoutInSeconds: Int     var defaultModuleEntries: [AnyObject]!     var authenticationModuleEntries: [AnyObject]!     var discoveryModuleEntries: [AnyObject]!     var generalModuleEntries: [AnyObject]!     convenience init!()     class func configuration() -> Self!     class func suggestedTrustAccount(_ hostname: String!) -> String!     class func suggestedTrustPassword(_ length: Int) -> String!     func saveUsingAuthorization(_ authorization: SFAuthorization!, error error: NSErrorPointer) -> Bool     func addTrustType(_ trustType: String!, trustAccount account: String!, trustPassword accountPassword: String!, username username: String!, password password: String!, joinExisting join: Bool, error error: NSErrorPointer) -> Bool     func removeTrustUsingUsername(_ username: String!, password password: String!, deleteTrustAccount deleteAccount: Bool, error error: NSErrorPointer) -> Bool } ``` |
| To | ``` class ODConfiguration : NSObject {     var nodeName: String!     var comment: String!     var defaultMappings: ODMappings!     var templateName: String!     var virtualSubnodes: [AnyObject]!     var hideRegistration: Bool     var preferredDestinationHostName: String!     var preferredDestinationHostPort: UInt16     var trustAccount: String! { get }     var trustMetaAccount: String! { get }     var trustKerberosPrincipal: String! { get }     var trustType: String! { get }     var trustUsesMutualAuthentication: Bool { get }     var trustUsesKerberosKeytab: Bool { get }     var trustUsesSystemKeychain: Bool { get }     var packetSigning: Int     var packetEncryption: Int     var manInTheMiddleProtection: Bool     var queryTimeoutInSeconds: Int     var connectionSetupTimeoutInSeconds: Int     var connectionIdleTimeoutInSeconds: Int     var defaultModuleEntries: [AnyObject]!     var authenticationModuleEntries: [AnyObject]!     var discoveryModuleEntries: [AnyObject]!     var generalModuleEntries: [AnyObject]!     convenience init!()     class func configuration() -> Self!     class func suggestedTrustAccount(_ hostname: String!) -> String!     class func suggestedTrustPassword(_ length: Int) -> String!     func saveUsingAuthorization(_ authorization: SFAuthorization!) throws     func addTrustType(_ trustType: String!, trustAccount account: String!, trustPassword accountPassword: String!, username username: String!, password password: String!, joinExisting join: Bool) throws     func removeTrustUsingUsername(_ username: String!, password password: String!, deleteTrustAccount deleteAccount: Bool) throws } ``` |

Modified [ODConfiguration.addTrustType(_: String!, trustAccount: String!, trustPassword: String!, username: String!, password: String!, joinExisting: Bool) throws](https://developer.apple.com/documentation/opendirectory/odconfiguration/1427863-addtrusttype)

|  | Declaration |
| --- | --- |
| From | ``` func addTrustType(_ trustType: String!, trustAccount account: String!, trustPassword accountPassword: String!, username username: String!, password password: String!, joinExisting join: Bool, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func addTrustType(_ trustType: String!, trustAccount account: String!, trustPassword accountPassword: String!, username username: String!, password password: String!, joinExisting join: Bool) throws ``` |

Modified [ODConfiguration.removeTrustUsingUsername(_: String!, password: String!, deleteTrustAccount: Bool) throws](https://developer.apple.com/documentation/opendirectory/odconfiguration/1426928-removetrust)

|  | Declaration |
| --- | --- |
| From | ``` func removeTrustUsingUsername(_ username: String!, password password: String!, deleteTrustAccount deleteAccount: Bool, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func removeTrustUsingUsername(_ username: String!, password password: String!, deleteTrustAccount deleteAccount: Bool) throws ``` |

Modified [ODConfiguration.saveUsingAuthorization(_: SFAuthorization!) throws](https://developer.apple.com/documentation/opendirectory/odconfiguration/1427633-save)

|  | Declaration |
| --- | --- |
| From | ``` func saveUsingAuthorization(_ authorization: SFAuthorization!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func saveUsingAuthorization(_ authorization: SFAuthorization!) throws ``` |

Modified [ODFrameworkErrors [struct]](https://developer.apple.com/documentation/opendirectory/odframeworkerrors)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ODFrameworkErrors {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct ODFrameworkErrors : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [ODNode](https://developer.apple.com/documentation/opendirectory/odnode)

|  | Declaration |
| --- | --- |
| From | ``` class ODNode : NSObject {     convenience init!(session inSession: ODSession!, type inType: ODNodeType, error outError: NSErrorPointer)     class func nodeWithSession(_ inSession: ODSession!, type inType: ODNodeType, error outError: NSErrorPointer) -> Self!     convenience init!(session inSession: ODSession!, name inName: String!, error outError: NSErrorPointer)     class func nodeWithSession(_ inSession: ODSession!, name inName: String!, error outError: NSErrorPointer) -> Self!     init!(session inSession: ODSession!, type inType: ODNodeType, error outError: NSErrorPointer)     init!(session inSession: ODSession!, name inName: String!, error outError: NSErrorPointer)     func subnodeNamesAndReturnError(_ outError: NSErrorPointer) -> [AnyObject]!     func unreachableSubnodeNamesAndReturnError(_ outError: NSErrorPointer) -> [AnyObject]!     var nodeName: String! { get }     func nodeDetailsForKeys(_ inKeys: [AnyObject]!, error outError: NSErrorPointer) -> [NSObject : AnyObject]!     func supportedRecordTypesAndReturnError(_ outError: NSErrorPointer) -> [AnyObject]!     func supportedAttributesForRecordType(_ inRecordType: String!, error outError: NSErrorPointer) -> [AnyObject]!     func setCredentialsWithRecordType(_ inRecordType: String!, recordName inRecordName: String!, password inPassword: String!, error outError: NSErrorPointer) -> Bool     func setCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>, error outError: NSErrorPointer) -> Bool     func setCredentialsUsingKerberosCache(_ inCacheName: String!, error outError: NSErrorPointer) -> Bool     func createRecordWithRecordType(_ inRecordType: String!, name inRecordName: String!, attributes inAttributes: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> ODRecord!     func recordWithRecordType(_ inRecordType: String!, name inRecordName: String!, attributes inAttributes: AnyObject!, error outError: NSErrorPointer) -> ODRecord!     func customCall(_ inCustomCode: Int, sendData inSendData: NSData!, error outError: NSErrorPointer) -> NSData!     func customFunction(_ function: String!, payload payload: AnyObject!, error error: NSErrorPointer) -> AnyObject!     var configuration: ODConfiguration! { get }     func policiesAndReturnError(_ error: NSErrorPointer) -> [NSObject : AnyObject]!     func supportedPoliciesAndReturnError(_ error: NSErrorPointer) -> [NSObject : AnyObject]!     func setPolicies(_ policies: [NSObject : AnyObject]!, error error: NSErrorPointer) -> Bool     func setPolicy(_ policy: ODPolicyType!, value value: AnyObject!, error error: NSErrorPointer) -> Bool     func removePolicy(_ policy: ODPolicyType!, error error: NSErrorPointer) -> Bool     func addAccountPolicy(_ policy: [NSObject : AnyObject]!, toCategory category: String!, error error: NSErrorPointer) -> Bool     func removeAccountPolicy(_ policy: [NSObject : AnyObject]!, fromCategory category: String!, error error: NSErrorPointer) -> Bool     func setAccountPolicies(_ policies: [NSObject : AnyObject]!, error error: NSErrorPointer) -> Bool     func accountPoliciesAndReturnError(_ error: NSErrorPointer) -> [NSObject : AnyObject]!     func passwordContentCheck(_ password: String!, forRecordName recordName: String!, error error: NSErrorPointer) -> Bool } ``` |
| To | ``` class ODNode : NSObject {     convenience init(session inSession: ODSession!, type inType: ODNodeType) throws     class func nodeWithSession(_ inSession: ODSession!, type inType: ODNodeType) throws -> Self     convenience init(session inSession: ODSession!, name inName: String!) throws     class func nodeWithSession(_ inSession: ODSession!, name inName: String!) throws -> Self     init(session inSession: ODSession!, type inType: ODNodeType) throws     init(session inSession: ODSession!, name inName: String!) throws     func subnodeNames() throws -> [AnyObject]     func unreachableSubnodeNames() throws -> [AnyObject]     var nodeName: String! { get }     func nodeDetailsForKeys(_ inKeys: [AnyObject]!) throws -> [NSObject : AnyObject]     func supportedRecordTypes() throws -> [AnyObject]     func supportedAttributesForRecordType(_ inRecordType: String!) throws -> [AnyObject]     func setCredentialsWithRecordType(_ inRecordType: String!, recordName inRecordName: String!, password inPassword: String!) throws     func setCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>) throws     func setCredentialsUsingKerberosCache(_ inCacheName: String!) throws     func createRecordWithRecordType(_ inRecordType: String!, name inRecordName: String!, attributes inAttributes: [NSObject : AnyObject]!) throws -> ODRecord     func recordWithRecordType(_ inRecordType: String!, name inRecordName: String!, attributes inAttributes: AnyObject!) throws -> ODRecord     func customCall(_ inCustomCode: Int, sendData inSendData: NSData!) throws -> NSData     func customFunction(_ function: String!, payload payload: AnyObject!) throws -> AnyObject     var configuration: ODConfiguration! { get }     func policies() throws -> [NSObject : AnyObject]     func supportedPolicies() throws -> [NSObject : AnyObject]     func setPolicies(_ policies: [NSObject : AnyObject]!) throws     func setPolicy(_ policy: ODPolicyType!, value value: AnyObject!) throws     func removePolicy(_ policy: ODPolicyType!) throws     func addAccountPolicy(_ policy: [NSObject : AnyObject]!, toCategory category: String!) throws     func removeAccountPolicy(_ policy: [NSObject : AnyObject]!, fromCategory category: String!) throws     func setAccountPolicies(_ policies: [NSObject : AnyObject]!) throws     func accountPolicies() throws -> [NSObject : AnyObject]     func passwordContentCheck(_ password: String!, forRecordName recordName: String!) throws } ``` |

Modified [ODNode.accountPolicies() throws -> [NSObject : AnyObject]](https://developer.apple.com/documentation/opendirectory/odnode/1428081-accountpoliciesandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func accountPoliciesAndReturnError(_ error: NSErrorPointer) -> [NSObject : AnyObject]! ``` |
| To | ``` func accountPolicies() throws -> [NSObject : AnyObject] ``` |

Modified [ODNode.addAccountPolicy(_: [NSObject : AnyObject]!, toCategory: String!) throws](https://developer.apple.com/documentation/opendirectory/odnode/1427951-addaccountpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func addAccountPolicy(_ policy: [NSObject : AnyObject]!, toCategory category: String!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func addAccountPolicy(_ policy: [NSObject : AnyObject]!, toCategory category: String!) throws ``` |

Modified [ODNode.createRecordWithRecordType(_: String!, name: String!, attributes: [NSObject : AnyObject]!) throws -> ODRecord](https://developer.apple.com/documentation/opendirectory/odnode/1427031-createrecordwithrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` func createRecordWithRecordType(_ inRecordType: String!, name inRecordName: String!, attributes inAttributes: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> ODRecord! ``` |
| To | ``` func createRecordWithRecordType(_ inRecordType: String!, name inRecordName: String!, attributes inAttributes: [NSObject : AnyObject]!) throws -> ODRecord ``` |

Modified [ODNode.customCall(_: Int, sendData: NSData!) throws -> NSData](https://developer.apple.com/documentation/opendirectory/odnode/1427478-customcall)

|  | Declaration |
| --- | --- |
| From | ``` func customCall(_ inCustomCode: Int, sendData inSendData: NSData!, error outError: NSErrorPointer) -> NSData! ``` |
| To | ``` func customCall(_ inCustomCode: Int, sendData inSendData: NSData!) throws -> NSData ``` |

Modified [ODNode.customFunction(_: String!, payload: AnyObject!) throws -> AnyObject](https://developer.apple.com/documentation/opendirectory/odnode/1427071-customfunction)

|  | Declaration |
| --- | --- |
| From | ``` func customFunction(_ function: String!, payload payload: AnyObject!, error error: NSErrorPointer) -> AnyObject! ``` |
| To | ``` func customFunction(_ function: String!, payload payload: AnyObject!) throws -> AnyObject ``` |

Modified [ODNode.init(session: ODSession!, name: String!) throws](https://developer.apple.com/documentation/opendirectory/odnode/1428278-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(session inSession: ODSession!, name inName: String!, error outError: NSErrorPointer) ``` |
| To | ``` init(session inSession: ODSession!, name inName: String!) throws ``` |

Modified [ODNode.init(session: ODSession!, type: ODNodeType) throws](https://developer.apple.com/documentation/opendirectory/odnode/1427701-initwithsession)

|  | Declaration |
| --- | --- |
| From | ``` init!(session inSession: ODSession!, type inType: ODNodeType, error outError: NSErrorPointer) ``` |
| To | ``` init(session inSession: ODSession!, type inType: ODNodeType) throws ``` |

Modified [ODNode.nodeDetailsForKeys(_: [AnyObject]!) throws -> [NSObject : AnyObject]](https://developer.apple.com/documentation/opendirectory/odnode/1427177-nodedetailsforkeys)

|  | Declaration |
| --- | --- |
| From | ``` func nodeDetailsForKeys(_ inKeys: [AnyObject]!, error outError: NSErrorPointer) -> [NSObject : AnyObject]! ``` |
| To | ``` func nodeDetailsForKeys(_ inKeys: [AnyObject]!) throws -> [NSObject : AnyObject] ``` |

Modified [ODNode.passwordContentCheck(_: String!, forRecordName: String!) throws](https://developer.apple.com/documentation/opendirectory/odnode/1427933-passwordcontentcheck)

|  | Declaration |
| --- | --- |
| From | ``` func passwordContentCheck(_ password: String!, forRecordName recordName: String!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func passwordContentCheck(_ password: String!, forRecordName recordName: String!) throws ``` |

Modified [ODNode.policies() throws -> [NSObject : AnyObject]](https://developer.apple.com/documentation/opendirectory/odnode/1428217-policies)

|  | Declaration |
| --- | --- |
| From | ``` func policiesAndReturnError(_ error: NSErrorPointer) -> [NSObject : AnyObject]! ``` |
| To | ``` func policies() throws -> [NSObject : AnyObject] ``` |

Modified [ODNode.recordWithRecordType(_: String!, name: String!, attributes: AnyObject!) throws -> ODRecord](https://developer.apple.com/documentation/opendirectory/odnode/1428065-record)

|  | Declaration |
| --- | --- |
| From | ``` func recordWithRecordType(_ inRecordType: String!, name inRecordName: String!, attributes inAttributes: AnyObject!, error outError: NSErrorPointer) -> ODRecord! ``` |
| To | ``` func recordWithRecordType(_ inRecordType: String!, name inRecordName: String!, attributes inAttributes: AnyObject!) throws -> ODRecord ``` |

Modified [ODNode.removeAccountPolicy(_: [NSObject : AnyObject]!, fromCategory: String!) throws](https://developer.apple.com/documentation/opendirectory/odnode/1427267-removeaccountpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func removeAccountPolicy(_ policy: [NSObject : AnyObject]!, fromCategory category: String!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func removeAccountPolicy(_ policy: [NSObject : AnyObject]!, fromCategory category: String!) throws ``` |

Modified [ODNode.removePolicy(_: ODPolicyType!) throws](https://developer.apple.com/documentation/opendirectory/odnode/1427245-removepolicy)

|  | Declaration |
| --- | --- |
| From | ``` func removePolicy(_ policy: ODPolicyType!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func removePolicy(_ policy: ODPolicyType!) throws ``` |

Modified [ODNode.setAccountPolicies(_: [NSObject : AnyObject]!) throws](https://developer.apple.com/documentation/opendirectory/odnode/1426999-setaccountpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func setAccountPolicies(_ policies: [NSObject : AnyObject]!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func setAccountPolicies(_ policies: [NSObject : AnyObject]!) throws ``` |

Modified [ODNode.setCredentialsUsingKerberosCache(_: String!) throws](https://developer.apple.com/documentation/opendirectory/odnode/1427785-setcredentialsusingkerberoscache)

|  | Declaration |
| --- | --- |
| From | ``` func setCredentialsUsingKerberosCache(_ inCacheName: String!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setCredentialsUsingKerberosCache(_ inCacheName: String!) throws ``` |

Modified [ODNode.setCredentialsWithRecordType(_: String!, authenticationType: String!, authenticationItems: [AnyObject]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context: AutoreleasingUnsafeMutablePointer<AnyObject?>) throws](https://developer.apple.com/documentation/opendirectory/odnode/1426987-setcredentialswithrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` func setCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>) throws ``` |

Modified [ODNode.setCredentialsWithRecordType(_: String!, recordName: String!, password: String!) throws](https://developer.apple.com/documentation/opendirectory/odnode/1427290-setcredentialswithrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` func setCredentialsWithRecordType(_ inRecordType: String!, recordName inRecordName: String!, password inPassword: String!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setCredentialsWithRecordType(_ inRecordType: String!, recordName inRecordName: String!, password inPassword: String!) throws ``` |

Modified [ODNode.setPolicies(_: [NSObject : AnyObject]!) throws](https://developer.apple.com/documentation/opendirectory/odnode/1426946-setpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func setPolicies(_ policies: [NSObject : AnyObject]!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func setPolicies(_ policies: [NSObject : AnyObject]!) throws ``` |

Modified [ODNode.setPolicy(_: ODPolicyType!, value: AnyObject!) throws](https://developer.apple.com/documentation/opendirectory/odnode/1428225-setpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func setPolicy(_ policy: ODPolicyType!, value value: AnyObject!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func setPolicy(_ policy: ODPolicyType!, value value: AnyObject!) throws ``` |

Modified [ODNode.subnodeNames() throws -> [AnyObject]](https://developer.apple.com/documentation/opendirectory/odnode/1428155-subnodenamesandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func subnodeNamesAndReturnError(_ outError: NSErrorPointer) -> [AnyObject]! ``` |
| To | ``` func subnodeNames() throws -> [AnyObject] ``` |

Modified [ODNode.supportedAttributesForRecordType(_: String!) throws -> [AnyObject]](https://developer.apple.com/documentation/opendirectory/odnode/1428017-supportedattributes)

|  | Declaration |
| --- | --- |
| From | ``` func supportedAttributesForRecordType(_ inRecordType: String!, error outError: NSErrorPointer) -> [AnyObject]! ``` |
| To | ``` func supportedAttributesForRecordType(_ inRecordType: String!) throws -> [AnyObject] ``` |

Modified [ODNode.supportedPolicies() throws -> [NSObject : AnyObject]](https://developer.apple.com/documentation/opendirectory/odnode/1428033-supportedpoliciesandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func supportedPoliciesAndReturnError(_ error: NSErrorPointer) -> [NSObject : AnyObject]! ``` |
| To | ``` func supportedPolicies() throws -> [NSObject : AnyObject] ``` |

Modified [ODNode.supportedRecordTypes() throws -> [AnyObject]](https://developer.apple.com/documentation/opendirectory/odnode/1427314-supportedrecordtypes)

|  | Declaration |
| --- | --- |
| From | ``` func supportedRecordTypesAndReturnError(_ outError: NSErrorPointer) -> [AnyObject]! ``` |
| To | ``` func supportedRecordTypes() throws -> [AnyObject] ``` |

Modified [ODNode.unreachableSubnodeNames() throws -> [AnyObject]](https://developer.apple.com/documentation/opendirectory/odnode/1427251-unreachablesubnodenamesandreturn)

|  | Declaration |
| --- | --- |
| From | ``` func unreachableSubnodeNamesAndReturnError(_ outError: NSErrorPointer) -> [AnyObject]! ``` |
| To | ``` func unreachableSubnodeNames() throws -> [AnyObject] ``` |

Modified [ODQuery](https://developer.apple.com/documentation/opendirectory/odquery)

|  | Declaration |
| --- | --- |
| From | ``` class ODQuery : NSObject, NSCopying {     init!(node inNode: ODNode!, forRecordTypes inRecordTypeOrList: AnyObject!, attribute inAttribute: String!, matchType inMatchType: ODMatchType, queryValues inQueryValueOrList: AnyObject!, returnAttributes inReturnAttributeOrList: AnyObject!, maximumResults inMaximumResults: Int, error outError: NSErrorPointer) -> ODQuery     class func queryWithNode(_ inNode: ODNode!, forRecordTypes inRecordTypeOrList: AnyObject!, attribute inAttribute: String!, matchType inMatchType: ODMatchType, queryValues inQueryValueOrList: AnyObject!, returnAttributes inReturnAttributeOrList: AnyObject!, maximumResults inMaximumResults: Int, error outError: NSErrorPointer) -> ODQuery!     init!(node inNode: ODNode!, forRecordTypes inRecordTypeOrList: AnyObject!, attribute inAttribute: String!, matchType inMatchType: ODMatchType, queryValues inQueryValueOrList: AnyObject!, returnAttributes inReturnAttributeOrList: AnyObject!, maximumResults inMaximumResults: Int, error outError: NSErrorPointer)     func resultsAllowingPartial(_ inAllowPartialResults: Bool, error outError: NSErrorPointer) -> [AnyObject]!     unowned(unsafe) var delegate: ODQueryDelegate!     func scheduleInRunLoop(_ inRunLoop: NSRunLoop!, forMode inMode: String!)     func removeFromRunLoop(_ inRunLoop: NSRunLoop!, forMode inMode: String!)     func synchronize()     var operationQueue: NSOperationQueue! } ``` |
| To | ``` class ODQuery : NSObject, NSCopying {      init(node inNode: ODNode!, forRecordTypes inRecordTypeOrList: AnyObject!, attribute inAttribute: String!, matchType inMatchType: ODMatchType, queryValues inQueryValueOrList: AnyObject!, returnAttributes inReturnAttributeOrList: AnyObject!, maximumResults inMaximumResults: Int) throws     class func queryWithNode(_ inNode: ODNode!, forRecordTypes inRecordTypeOrList: AnyObject!, attribute inAttribute: String!, matchType inMatchType: ODMatchType, queryValues inQueryValueOrList: AnyObject!, returnAttributes inReturnAttributeOrList: AnyObject!, maximumResults inMaximumResults: Int) throws -> ODQuery     init(node inNode: ODNode!, forRecordTypes inRecordTypeOrList: AnyObject!, attribute inAttribute: String!, matchType inMatchType: ODMatchType, queryValues inQueryValueOrList: AnyObject!, returnAttributes inReturnAttributeOrList: AnyObject!, maximumResults inMaximumResults: Int) throws     func resultsAllowingPartial(_ inAllowPartialResults: Bool) throws -> [AnyObject]     unowned(unsafe) var delegate: ODQueryDelegate!     func scheduleInRunLoop(_ inRunLoop: NSRunLoop!, forMode inMode: String!)     func removeFromRunLoop(_ inRunLoop: NSRunLoop!, forMode inMode: String!)     func synchronize()     var operationQueue: NSOperationQueue! } ``` |

Modified [ODQuery.init(node: ODNode!, forRecordTypes: AnyObject!, attribute: String!, matchType: ODMatchType, queryValues: AnyObject!, returnAttributes: AnyObject!, maximumResults: Int) throws](https://developer.apple.com/documentation/opendirectory/odquery/1391711-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(node inNode: ODNode!, forRecordTypes inRecordTypeOrList: AnyObject!, attribute inAttribute: String!, matchType inMatchType: ODMatchType, queryValues inQueryValueOrList: AnyObject!, returnAttributes inReturnAttributeOrList: AnyObject!, maximumResults inMaximumResults: Int, error outError: NSErrorPointer) ``` |
| To | ``` init(node inNode: ODNode!, forRecordTypes inRecordTypeOrList: AnyObject!, attribute inAttribute: String!, matchType inMatchType: ODMatchType, queryValues inQueryValueOrList: AnyObject!, returnAttributes inReturnAttributeOrList: AnyObject!, maximumResults inMaximumResults: Int) throws ``` |

Modified [ODQuery.resultsAllowingPartial(_: Bool) throws -> [AnyObject]](https://developer.apple.com/documentation/opendirectory/odquery/1391702-resultsallowingpartial)

|  | Declaration |
| --- | --- |
| From | ``` func resultsAllowingPartial(_ inAllowPartialResults: Bool, error outError: NSErrorPointer) -> [AnyObject]! ``` |
| To | ``` func resultsAllowingPartial(_ inAllowPartialResults: Bool) throws -> [AnyObject] ``` |

Modified [ODRecord](https://developer.apple.com/documentation/opendirectory/odrecord)

|  | Declaration |
| --- | --- |
| From | ``` class ODRecord : NSObject {     func setNodeCredentials(_ inUsername: String!, password inPassword: String!, error outError: NSErrorPointer) -> Bool     func setNodeCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>, error outError: NSErrorPointer) -> Bool     func setNodeCredentialsUsingKerberosCache(_ inCacheName: String!, error outError: NSErrorPointer) -> Bool     func passwordPolicyAndReturnError(_ outError: NSErrorPointer) -> [NSObject : AnyObject]!     func verifyPassword(_ inPassword: String!, error outError: NSErrorPointer) -> Bool     func verifyExtendedWithAuthenticationType(_ inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>, error outError: NSErrorPointer) -> Bool     func changePassword(_ oldPassword: String!, toPassword newPassword: String!, error outError: NSErrorPointer) -> Bool     func synchronizeAndReturnError(_ outError: NSErrorPointer) -> Bool     var recordType: String! { get }     var recordName: String! { get }     func recordDetailsForAttributes(_ inAttributes: [AnyObject]!, error outError: NSErrorPointer) -> [NSObject : AnyObject]!     func valuesForAttribute(_ inAttribute: String!, error outError: NSErrorPointer) -> [AnyObject]!     func setValue(_ inValueOrValues: AnyObject!, forAttribute inAttribute: String!, error outError: NSErrorPointer) -> Bool     func removeValuesForAttribute(_ inAttribute: String!, error outError: NSErrorPointer) -> Bool     func addValue(_ inValue: AnyObject!, toAttribute inAttribute: String!, error outError: NSErrorPointer) -> Bool     func removeValue(_ inValue: AnyObject!, fromAttribute inAttribute: String!, error outError: NSErrorPointer) -> Bool     func deleteRecordAndReturnError(_ outError: NSErrorPointer) -> Bool     func policiesAndReturnError(_ error: NSErrorPointer) -> [NSObject : AnyObject]!     func effectivePoliciesAndReturnError(_ error: NSErrorPointer) -> [NSObject : AnyObject]!     func supportedPoliciesAndReturnError(_ error: NSErrorPointer) -> [NSObject : AnyObject]!     func setPolicies(_ policies: [NSObject : AnyObject]!, error error: NSErrorPointer) -> Bool     func setPolicy(_ policy: ODPolicyType!, value value: AnyObject!, error error: NSErrorPointer) -> Bool     func removePolicy(_ policy: ODPolicyType!, error error: NSErrorPointer) -> Bool     func addAccountPolicy(_ policy: [NSObject : AnyObject]!, toCategory category: String!, error error: NSErrorPointer) -> Bool     func removeAccountPolicy(_ policy: [NSObject : AnyObject]!, fromCategory category: String!, error error: NSErrorPointer) -> Bool     func setAccountPolicies(_ policies: [NSObject : AnyObject]!, error error: NSErrorPointer) -> Bool     func accountPoliciesAndReturnError(_ error: NSErrorPointer) -> [NSObject : AnyObject]!     func authenticationAllowedAndReturnError(_ error: NSErrorPointer) -> Bool     func passwordChangeAllowed(_ newPassword: String!, error error: NSErrorPointer) -> Bool     func willPasswordExpire(_ willExpireIn: UInt64) -> Bool     func willAuthenticationsExpire(_ willExpireIn: UInt64) -> Bool     var secondsUntilPasswordExpires: Int64 { get }     var secondsUntilAuthenticationsExpire: Int64 { get } } extension ODRecord {     func addMemberRecord(_ inRecord: ODRecord!, error outError: NSErrorPointer) -> Bool     func removeMemberRecord(_ inRecord: ODRecord!, error outError: NSErrorPointer) -> Bool     func isMemberRecord(_ inRecord: ODRecord!, error outError: NSErrorPointer) -> Bool } ``` |
| To | ``` class ODRecord : NSObject {     func setNodeCredentials(_ inUsername: String!, password inPassword: String!) throws     func setNodeCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>) throws     func setNodeCredentialsUsingKerberosCache(_ inCacheName: String!) throws     func passwordPolicy() throws -> [NSObject : AnyObject]     func verifyPassword(_ inPassword: String!) throws     func verifyExtendedWithAuthenticationType(_ inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>) throws     func changePassword(_ oldPassword: String!, toPassword newPassword: String!) throws     func synchronize() throws     var recordType: String! { get }     var recordName: String! { get }     func recordDetailsForAttributes(_ inAttributes: [AnyObject]!) throws -> [NSObject : AnyObject]     func valuesForAttribute(_ inAttribute: String!) throws -> [AnyObject]     func setValue(_ inValueOrValues: AnyObject!, forAttribute inAttribute: String!) throws     func removeValuesForAttribute(_ inAttribute: String!) throws     func addValue(_ inValue: AnyObject!, toAttribute inAttribute: String!) throws     func removeValue(_ inValue: AnyObject!, fromAttribute inAttribute: String!) throws     func deleteRecord() throws     func policies() throws -> [NSObject : AnyObject]     func effectivePolicies() throws -> [NSObject : AnyObject]     func supportedPolicies() throws -> [NSObject : AnyObject]     func setPolicies(_ policies: [NSObject : AnyObject]!) throws     func setPolicy(_ policy: ODPolicyType!, value value: AnyObject!) throws     func removePolicy(_ policy: ODPolicyType!) throws     func addAccountPolicy(_ policy: [NSObject : AnyObject]!, toCategory category: String!) throws     func removeAccountPolicy(_ policy: [NSObject : AnyObject]!, fromCategory category: String!) throws     func setAccountPolicies(_ policies: [NSObject : AnyObject]!) throws     func accountPolicies() throws -> [NSObject : AnyObject]     func authenticationAllowed() throws     func passwordChangeAllowed(_ newPassword: String!) throws     func willPasswordExpire(_ willExpireIn: UInt64) -> Bool     func willAuthenticationsExpire(_ willExpireIn: UInt64) -> Bool     var secondsUntilPasswordExpires: Int64 { get }     var secondsUntilAuthenticationsExpire: Int64 { get } } extension ODRecord {     func addMemberRecord(_ inRecord: ODRecord!) throws     func removeMemberRecord(_ inRecord: ODRecord!) throws     func isMemberRecord(_ inRecord: ODRecord!) throws } ``` |

Modified [ODRecord.accountPolicies() throws -> [NSObject : AnyObject]](https://developer.apple.com/documentation/opendirectory/odrecord/1428124-accountpoliciesandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func accountPoliciesAndReturnError(_ error: NSErrorPointer) -> [NSObject : AnyObject]! ``` |
| To | ``` func accountPolicies() throws -> [NSObject : AnyObject] ``` |

Modified [ODRecord.addAccountPolicy(_: [NSObject : AnyObject]!, toCategory: String!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427406-addaccountpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func addAccountPolicy(_ policy: [NSObject : AnyObject]!, toCategory category: String!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func addAccountPolicy(_ policy: [NSObject : AnyObject]!, toCategory category: String!) throws ``` |

Modified [ODRecord.addMemberRecord(_: ODRecord!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427807-addmemberrecord)

|  | Declaration |
| --- | --- |
| From | ``` func addMemberRecord(_ inRecord: ODRecord!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func addMemberRecord(_ inRecord: ODRecord!) throws ``` |

Modified [ODRecord.addValue(_: AnyObject!, toAttribute: String!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427729-addvalue)

|  | Declaration |
| --- | --- |
| From | ``` func addValue(_ inValue: AnyObject!, toAttribute inAttribute: String!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func addValue(_ inValue: AnyObject!, toAttribute inAttribute: String!) throws ``` |

Modified [ODRecord.authenticationAllowed() throws](https://developer.apple.com/documentation/opendirectory/odrecord/1428106-authenticationallowedandreturner)

|  | Declaration |
| --- | --- |
| From | ``` func authenticationAllowedAndReturnError(_ error: NSErrorPointer) -> Bool ``` |
| To | ``` func authenticationAllowed() throws ``` |

Modified [ODRecord.changePassword(_: String!, toPassword: String!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427145-changepassword)

|  | Declaration |
| --- | --- |
| From | ``` func changePassword(_ oldPassword: String!, toPassword newPassword: String!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func changePassword(_ oldPassword: String!, toPassword newPassword: String!) throws ``` |

Modified [ODRecord.deleteRecord() throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427488-deleterecordandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func deleteRecordAndReturnError(_ outError: NSErrorPointer) -> Bool ``` |
| To | ``` func deleteRecord() throws ``` |

Modified [ODRecord.effectivePolicies() throws -> [NSObject : AnyObject]](https://developer.apple.com/documentation/opendirectory/odrecord/1427296-effectivepoliciesandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func effectivePoliciesAndReturnError(_ error: NSErrorPointer) -> [NSObject : AnyObject]! ``` |
| To | ``` func effectivePolicies() throws -> [NSObject : AnyObject] ``` |

Modified [ODRecord.isMemberRecord(_: ODRecord!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427975-ismemberrecord)

|  | Declaration |
| --- | --- |
| From | ``` func isMemberRecord(_ inRecord: ODRecord!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func isMemberRecord(_ inRecord: ODRecord!) throws ``` |

Modified [ODRecord.passwordChangeAllowed(_: String!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427623-passwordchangeallowed)

|  | Declaration |
| --- | --- |
| From | ``` func passwordChangeAllowed(_ newPassword: String!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func passwordChangeAllowed(_ newPassword: String!) throws ``` |

Modified [ODRecord.policies() throws -> [NSObject : AnyObject]](https://developer.apple.com/documentation/opendirectory/odrecord/1427995-policiesandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func policiesAndReturnError(_ error: NSErrorPointer) -> [NSObject : AnyObject]! ``` |
| To | ``` func policies() throws -> [NSObject : AnyObject] ``` |

Modified [ODRecord.recordDetailsForAttributes(_: [AnyObject]!) throws -> [NSObject : AnyObject]](https://developer.apple.com/documentation/opendirectory/odrecord/1427081-recorddetails)

|  | Declaration |
| --- | --- |
| From | ``` func recordDetailsForAttributes(_ inAttributes: [AnyObject]!, error outError: NSErrorPointer) -> [NSObject : AnyObject]! ``` |
| To | ``` func recordDetailsForAttributes(_ inAttributes: [AnyObject]!) throws -> [NSObject : AnyObject] ``` |

Modified [ODRecord.removeAccountPolicy(_: [NSObject : AnyObject]!, fromCategory: String!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427577-removeaccountpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func removeAccountPolicy(_ policy: [NSObject : AnyObject]!, fromCategory category: String!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func removeAccountPolicy(_ policy: [NSObject : AnyObject]!, fromCategory category: String!) throws ``` |

Modified [ODRecord.removeMemberRecord(_: ODRecord!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427555-removememberrecord)

|  | Declaration |
| --- | --- |
| From | ``` func removeMemberRecord(_ inRecord: ODRecord!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func removeMemberRecord(_ inRecord: ODRecord!) throws ``` |

Modified [ODRecord.removePolicy(_: ODPolicyType!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427589-removepolicy)

|  | Declaration |
| --- | --- |
| From | ``` func removePolicy(_ policy: ODPolicyType!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func removePolicy(_ policy: ODPolicyType!) throws ``` |

Modified [ODRecord.removeValue(_: AnyObject!, fromAttribute: String!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1428290-removevalue)

|  | Declaration |
| --- | --- |
| From | ``` func removeValue(_ inValue: AnyObject!, fromAttribute inAttribute: String!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func removeValue(_ inValue: AnyObject!, fromAttribute inAttribute: String!) throws ``` |

Modified [ODRecord.removeValuesForAttribute(_: String!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427273-removevalues)

|  | Declaration |
| --- | --- |
| From | ``` func removeValuesForAttribute(_ inAttribute: String!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func removeValuesForAttribute(_ inAttribute: String!) throws ``` |

Modified [ODRecord.setAccountPolicies(_: [NSObject : AnyObject]!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427241-setaccountpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func setAccountPolicies(_ policies: [NSObject : AnyObject]!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func setAccountPolicies(_ policies: [NSObject : AnyObject]!) throws ``` |

Modified [ODRecord.setNodeCredentials(_: String!, password: String!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427258-setnodecredentials)

|  | Declaration |
| --- | --- |
| From | ``` func setNodeCredentials(_ inUsername: String!, password inPassword: String!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setNodeCredentials(_ inUsername: String!, password inPassword: String!) throws ``` |

Modified [ODRecord.setNodeCredentialsWithRecordType(_: String!, authenticationType: String!, authenticationItems: [AnyObject]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context: AutoreleasingUnsafeMutablePointer<AnyObject?>) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427282-setnodecredentialswithrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` func setNodeCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setNodeCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>) throws ``` |

Modified [ODRecord.setPolicies(_: [NSObject : AnyObject]!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427266-setpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func setPolicies(_ policies: [NSObject : AnyObject]!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func setPolicies(_ policies: [NSObject : AnyObject]!) throws ``` |

Modified [ODRecord.setPolicy(_: ODPolicyType!, value: AnyObject!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427191-setpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func setPolicy(_ policy: ODPolicyType!, value value: AnyObject!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func setPolicy(_ policy: ODPolicyType!, value value: AnyObject!) throws ``` |

Modified [ODRecord.setValue(_: AnyObject!, forAttribute: String!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427911-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` func setValue(_ inValueOrValues: AnyObject!, forAttribute inAttribute: String!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setValue(_ inValueOrValues: AnyObject!, forAttribute inAttribute: String!) throws ``` |

Modified [ODRecord.supportedPolicies() throws -> [NSObject : AnyObject]](https://developer.apple.com/documentation/opendirectory/odrecord/1428172-supportedpoliciesandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func supportedPoliciesAndReturnError(_ error: NSErrorPointer) -> [NSObject : AnyObject]! ``` |
| To | ``` func supportedPolicies() throws -> [NSObject : AnyObject] ``` |

Modified [ODRecord.synchronize() throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427579-synchronizeandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func synchronizeAndReturnError(_ outError: NSErrorPointer) -> Bool ``` |
| To | ``` func synchronize() throws ``` |

Modified [ODRecord.valuesForAttribute(_: String!) throws -> [AnyObject]](https://developer.apple.com/documentation/opendirectory/odrecord/1427803-values)

|  | Declaration |
| --- | --- |
| From | ``` func valuesForAttribute(_ inAttribute: String!, error outError: NSErrorPointer) -> [AnyObject]! ``` |
| To | ``` func valuesForAttribute(_ inAttribute: String!) throws -> [AnyObject] ``` |

Modified [ODRecord.verifyExtendedWithAuthenticationType(_: String!, authenticationItems: [AnyObject]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context: AutoreleasingUnsafeMutablePointer<AnyObject?>) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427575-verifyextendedwithauthentication)

|  | Declaration |
| --- | --- |
| From | ``` func verifyExtendedWithAuthenticationType(_ inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func verifyExtendedWithAuthenticationType(_ inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>) throws ``` |

Modified [ODRecord.verifyPassword(_: String!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427894-verifypassword)

|  | Declaration |
| --- | --- |
| From | ``` func verifyPassword(_ inPassword: String!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func verifyPassword(_ inPassword: String!) throws ``` |

Modified [ODSession](https://developer.apple.com/documentation/opendirectory/odsession)

|  | Declaration |
| --- | --- |
| From | ``` class ODSession : NSObject {     class func defaultSession() -> ODSession!     convenience init!(options inOptions: [NSObject : AnyObject]!, error outError: NSErrorPointer)     class func sessionWithOptions(_ inOptions: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> Self!     init!(options inOptions: [NSObject : AnyObject]!, error outError: NSErrorPointer)     func nodeNamesAndReturnError(_ outError: NSErrorPointer) -> [AnyObject]!     var configurationTemplateNames: [AnyObject]! { get }     var mappingTemplateNames: [AnyObject]! { get }     func configurationAuthorizationAllowingUserInteraction(_ allowInteraction: Bool, error error: NSErrorPointer) -> SFAuthorization!     func configurationForNodename(_ nodename: String!) -> ODConfiguration!     func addConfiguration(_ configuration: ODConfiguration!, authorization authorization: SFAuthorization!, error error: NSErrorPointer) -> Bool     func deleteConfiguration(_ configuration: ODConfiguration!, authorization authorization: SFAuthorization!, error error: NSErrorPointer) -> Bool     func deleteConfigurationWithNodename(_ nodename: String!, authorization authorization: SFAuthorization!, error error: NSErrorPointer) -> Bool } ``` |
| To | ``` class ODSession : NSObject {     class func defaultSession() -> ODSession!     convenience init(options inOptions: [NSObject : AnyObject]!) throws     class func sessionWithOptions(_ inOptions: [NSObject : AnyObject]!) throws -> Self     init(options inOptions: [NSObject : AnyObject]!) throws     func nodeNames() throws -> [AnyObject]     var configurationTemplateNames: [AnyObject]! { get }     var mappingTemplateNames: [AnyObject]! { get }     func configurationAuthorizationAllowingUserInteraction(_ allowInteraction: Bool) throws -> SFAuthorization     func configurationForNodename(_ nodename: String!) -> ODConfiguration!     func addConfiguration(_ configuration: ODConfiguration!, authorization authorization: SFAuthorization!) throws     func deleteConfiguration(_ configuration: ODConfiguration!, authorization authorization: SFAuthorization!) throws     func deleteConfigurationWithNodename(_ nodename: String!, authorization authorization: SFAuthorization!) throws } ``` |

Modified [ODSession.addConfiguration(_: ODConfiguration!, authorization: SFAuthorization!) throws](https://developer.apple.com/documentation/opendirectory/odsession/1427913-addconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` func addConfiguration(_ configuration: ODConfiguration!, authorization authorization: SFAuthorization!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func addConfiguration(_ configuration: ODConfiguration!, authorization authorization: SFAuthorization!) throws ``` |

Modified [ODSession.configurationAuthorizationAllowingUserInteraction(_: Bool) throws -> SFAuthorization](https://developer.apple.com/documentation/opendirectory/odsession/1428063-configurationauthorizationallowi)

|  | Declaration |
| --- | --- |
| From | ``` func configurationAuthorizationAllowingUserInteraction(_ allowInteraction: Bool, error error: NSErrorPointer) -> SFAuthorization! ``` |
| To | ``` func configurationAuthorizationAllowingUserInteraction(_ allowInteraction: Bool) throws -> SFAuthorization ``` |

Modified [ODSession.deleteConfiguration(_: ODConfiguration!, authorization: SFAuthorization!) throws](https://developer.apple.com/documentation/opendirectory/odsession/1428166-delete)

|  | Declaration |
| --- | --- |
| From | ``` func deleteConfiguration(_ configuration: ODConfiguration!, authorization authorization: SFAuthorization!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func deleteConfiguration(_ configuration: ODConfiguration!, authorization authorization: SFAuthorization!) throws ``` |

Modified [ODSession.deleteConfigurationWithNodename(_: String!, authorization: SFAuthorization!) throws](https://developer.apple.com/documentation/opendirectory/odsession/1427476-deleteconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` func deleteConfigurationWithNodename(_ nodename: String!, authorization authorization: SFAuthorization!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func deleteConfigurationWithNodename(_ nodename: String!, authorization authorization: SFAuthorization!) throws ``` |

Modified [ODSession.init(options: [NSObject : AnyObject]!) throws](https://developer.apple.com/documentation/opendirectory/odsession/1427223-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(options inOptions: [NSObject : AnyObject]!, error outError: NSErrorPointer) ``` |
| To | ``` init(options inOptions: [NSObject : AnyObject]!) throws ``` |

Modified [ODSession.nodeNames() throws -> [AnyObject]](https://developer.apple.com/documentation/opendirectory/odsession/1427490-nodenamesandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func nodeNamesAndReturnError(_ outError: NSErrorPointer) -> [AnyObject]! ``` |
| To | ``` func nodeNames() throws -> [AnyObject] ``` |

Modified [ODQueryCallback](https://developer.apple.com/documentation/opendirectory/odquerycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias ODQueryCallback = CFunctionPointer<((ODQuery!, CFArray!, CFError!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias ODQueryCallback = (ODQuery!, CFArray!, CFError!, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [ODQuerySetCallback(_: ODQuery!, _: ODQueryCallback!, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/opendirectory/1427306-odquerysetcallback)

|  | Declaration |
| --- | --- |
| From | ``` func ODQuerySetCallback(_ query: ODQuery!, _ callback: ODQueryCallback, _ userInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func ODQuerySetCallback(_ query: ODQuery!, _ callback: ODQueryCallback!, _ userInfo: UnsafeMutablePointer<Void>) ``` |

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
