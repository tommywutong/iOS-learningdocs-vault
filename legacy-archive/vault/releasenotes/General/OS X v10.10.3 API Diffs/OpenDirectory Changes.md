---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/OpenDirectory.html
archived_at: '2026-07-18T02:52:34.795917Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# OpenDirectory Changes

## OpenDirectory

Removed ODNode.nodeWithSession(ODSession!, name: String!, error: NSErrorPointer) -> Self! [class]Removed ODNode.nodeWithSession(ODSession!, type: ODNodeType, error: NSErrorPointer) -> Self! [class]Removed ODQuery.queryWithNode(ODNode!, forRecordTypes: AnyObject!, attribute: String!, matchType: ODMatchType, queryValues: AnyObject!, returnAttributes: AnyObject!, maximumResults: Int, error: NSErrorPointer) -> ODQuery! [class]Removed ODSession.sessionWithOptions([NSObject: AnyObject]!, error: NSErrorPointer) -> Self! [class]Added ODConfiguration.saveUsingAuthorization(SFAuthorization!, error: NSErrorPointer) -> BoolAdded ODSession.addConfiguration(ODConfiguration!, authorization: SFAuthorization!, error: NSErrorPointer) -> BoolAdded ODSession.configurationAuthorizationAllowingUserInteraction(Bool, error: NSErrorPointer) -> SFAuthorization!Added ODSession.deleteConfiguration(ODConfiguration!, authorization: SFAuthorization!, error: NSErrorPointer) -> BoolAdded ODSession.deleteConfigurationWithNodename(String!, authorization: SFAuthorization!, error: NSErrorPointer) -> BoolModified ODAttributeMap

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODAttributeMap.customAttributes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODAttributeMap.customQueryFunction

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODAttributeMap.customTranslationFunction

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODAttributeMap.setStaticValue(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODAttributeMap.setVariableSubstitution(String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODAttributeMap.init(staticValue: String!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(staticValue staticValue: String!) ``` |
| To | ``` convenience init!(staticValue staticValue: String!) ``` |

Modified ODAttributeMap.value

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODAttributeMap.init(value: String!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(value value: String!) ``` |
| To | ``` convenience init!(value value: String!) ``` |

Modified ODConfiguration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.addTrustType(String!, trustAccount: String!, trustPassword: String!, username: String!, password: String!, joinExisting: Bool, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.authenticationModuleEntries

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.comment

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.connectionIdleTimeoutInSeconds

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.connectionSetupTimeoutInSeconds

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.defaultMappings

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.defaultModuleEntries

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.discoveryModuleEntries

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.generalModuleEntries

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.hideRegistration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.manInTheMiddleProtection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.nodeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.packetEncryption

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.packetSigning

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.preferredDestinationHostName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.preferredDestinationHostPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.queryTimeoutInSeconds

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.removeTrustUsingUsername(String!, password: String!, deleteTrustAccount: Bool, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.suggestedTrustAccount(String!) -> String! [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.suggestedTrustPassword(Int) -> String! [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func suggestedTrustPassword(_ length: UInt) -> String! ``` | OS X 10.10 |
| To | ``` class func suggestedTrustPassword(_ length: Int) -> String! ``` | OS X 10.9 |

Modified ODConfiguration.templateName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.trustAccount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.trustKerberosPrincipal

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.trustMetaAccount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.trustType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.trustUsesKerberosKeytab

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.trustUsesMutualAuthentication

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.trustUsesSystemKeychain

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODConfiguration.virtualSubnodes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODMappings

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODMappings.comment

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODMappings.function

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODMappings.functionAttributes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODMappings.identifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODMappings.recordMapForStandardRecordType(String!) -> ODRecordMap!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODMappings.recordTypes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODMappings.setRecordMap(ODRecordMap!, forStandardRecordType: String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODMappings.templateName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODModuleEntry

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODModuleEntry.mappings

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODModuleEntry.name

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODModuleEntry.init(name: String!, xpcServiceName: String!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(name name: String!, xpcServiceName xpcServiceName: String!) ``` | OS X 10.10 |
| To | ``` convenience init!(name name: String!, xpcServiceName xpcServiceName: String!) ``` | OS X 10.9 |

Modified ODModuleEntry.option(String!) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODModuleEntry.setOption(String!, value: AnyObject!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODModuleEntry.supportedOptions

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODModuleEntry.uuidString

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODModuleEntry.xpcServiceName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODNode.createRecordWithRecordType(String!, name: String!, attributes:[NSObject: AnyObject]!, error: NSErrorPointer) -> ODRecord!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODNode.customCall(Int, sendData: NSData!, error: NSErrorPointer) -> NSData!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODNode.customFunction(String!, payload: AnyObject!, error: NSErrorPointer) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODNode.nodeDetailsForKeys([AnyObject]!, error: NSErrorPointer) -> [NSObject: AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODNode.nodeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODNode.policiesAndReturnError(NSErrorPointer) -> [NSObject: AnyObject]!

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | OS X 10.10 |

Modified ODNode.recordWithRecordType(String!, name: String!, attributes: AnyObject!, error: NSErrorPointer) -> ODRecord!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODNode.removePolicy(ODPolicyType!, error: NSErrorPointer) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | OS X 10.10 |

Modified ODNode.init(session: ODSession!, name: String!, error: NSErrorPointer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(session inSession: ODSession!, name inName: String!, error outError: NSErrorPointer) ``` | OS X 10.10 |
| To | ``` init!(session inSession: ODSession!, name inName: String!, error outError: NSErrorPointer) ``` | OS X 10.6 |

Modified ODNode.init(session: ODSession!, type: ODNodeType, error: NSErrorPointer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(session inSession: ODSession!, type inType: ODNodeType, error outError: NSErrorPointer) ``` | OS X 10.10 |
| To | ``` init!(session inSession: ODSession!, type inType: ODNodeType, error outError: NSErrorPointer) ``` | OS X 10.6 |

Modified ODNode.setCredentialsUsingKerberosCache(String!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODNode.setCredentialsWithRecordType(String!, authenticationType: String!, authenticationItems:[AnyObject]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context: AutoreleasingUnsafeMutablePointer<AnyObject?>, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafePointer<NSArray?>, context outContext: AutoreleasingUnsafePointer<AnyObject?>, error outError: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func setCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>, error outError: NSErrorPointer) -> Bool ``` | OS X 10.6 |

Modified ODNode.setCredentialsWithRecordType(String!, recordName: String!, password: String!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODNode.setPolicies([NSObject: AnyObject]!, error: NSErrorPointer) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | OS X 10.10 |

Modified ODNode.setPolicy(ODPolicyType!, value: AnyObject!, error: NSErrorPointer) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | OS X 10.10 |

Modified ODNode.subnodeNamesAndReturnError(NSErrorPointer) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODNode.supportedAttributesForRecordType(String!, error: NSErrorPointer) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODNode.supportedPoliciesAndReturnError(NSErrorPointer) -> [NSObject: AnyObject]!

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | OS X 10.10 |

Modified ODNode.supportedRecordTypesAndReturnError(NSErrorPointer) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODNode.unreachableSubnodeNamesAndReturnError(NSErrorPointer) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODQuery.delegate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var delegate: ODQueryDelegate! ``` | OS X 10.10 |
| To | ``` unowned(unsafe) var delegate: ODQueryDelegate! ``` | OS X 10.6 |

Modified ODQuery.init(node: ODNode!, forRecordTypes: AnyObject!, attribute: String!, matchType: ODMatchType, queryValues: AnyObject!, returnAttributes: AnyObject!, maximumResults: Int, error: NSErrorPointer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(node inNode: ODNode!, forRecordTypes inRecordTypeOrList: AnyObject!, attribute inAttribute: String!, matchType inMatchType: ODMatchType, queryValues inQueryValueOrList: AnyObject!, returnAttributes inReturnAttributeOrList: AnyObject!, maximumResults inMaximumResults: Int, error outError: NSErrorPointer) ``` | OS X 10.10 |
| To | ``` init!(node inNode: ODNode!, forRecordTypes inRecordTypeOrList: AnyObject!, attribute inAttribute: String!, matchType inMatchType: ODMatchType, queryValues inQueryValueOrList: AnyObject!, returnAttributes inReturnAttributeOrList: AnyObject!, maximumResults inMaximumResults: Int, error outError: NSErrorPointer) ``` | OS X 10.6 |

Modified ODQuery.operationQueue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODQuery.removeFromRunLoop(NSRunLoop!, forMode: String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODQuery.resultsAllowingPartial(Bool, error: NSErrorPointer) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODQuery.scheduleInRunLoop(NSRunLoop!, forMode: String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODQuery.synchronize()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODQueryDelegate.query(ODQuery!, foundResults:[AnyObject]!, error: NSError!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecord.addMemberRecord(ODRecord!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecord.addValue(AnyObject!, toAttribute: String!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecord.changePassword(String!, toPassword: String!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecord.deleteRecordAndReturnError(NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecord.effectivePoliciesAndReturnError(NSErrorPointer) -> [NSObject: AnyObject]!

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | OS X 10.10 |

Modified ODRecord.isMemberRecord(ODRecord!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecord.policiesAndReturnError(NSErrorPointer) -> [NSObject: AnyObject]!

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | OS X 10.10 |

Modified ODRecord.recordDetailsForAttributes([AnyObject]!, error: NSErrorPointer) -> [NSObject: AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecord.recordName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecord.recordType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecord.removeMemberRecord(ODRecord!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecord.removePolicy(ODPolicyType!, error: NSErrorPointer) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | OS X 10.10 |

Modified ODRecord.removeValue(AnyObject!, fromAttribute: String!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecord.removeValuesForAttribute(String!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecord.setNodeCredentials(String!, password: String!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecord.setNodeCredentialsWithRecordType(String!, authenticationType: String!, authenticationItems:[AnyObject]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context: AutoreleasingUnsafeMutablePointer<AnyObject?>, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setNodeCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafePointer<NSArray?>, context outContext: AutoreleasingUnsafePointer<AnyObject?>, error outError: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func setNodeCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>, error outError: NSErrorPointer) -> Bool ``` | OS X 10.6 |

Modified ODRecord.setPolicies([NSObject: AnyObject]!, error: NSErrorPointer) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | OS X 10.10 |

Modified ODRecord.setPolicy(ODPolicyType!, value: AnyObject!, error: NSErrorPointer) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | OS X 10.10 |

Modified ODRecord.setValue(AnyObject!, forAttribute: String!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecord.supportedPoliciesAndReturnError(NSErrorPointer) -> [NSObject: AnyObject]!

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | OS X 10.10 |

Modified ODRecord.synchronizeAndReturnError(NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecord.valuesForAttribute(String!, error: NSErrorPointer) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecord.verifyExtendedWithAuthenticationType(String!, authenticationItems:[AnyObject]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context: AutoreleasingUnsafeMutablePointer<AnyObject?>, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func verifyExtendedWithAuthenticationType(_ inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafePointer<NSArray?>, context outContext: AutoreleasingUnsafePointer<AnyObject?>, error outError: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func verifyExtendedWithAuthenticationType(_ inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>, error outError: NSErrorPointer) -> Bool ``` | OS X 10.6 |

Modified ODRecord.verifyPassword(String!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecordMap

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODRecordMap.attributeMapForStandardAttribute(String!) -> ODAttributeMap!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODRecordMap.attributes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODRecordMap.native

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODRecordMap.odPredicate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODRecordMap.setAttributeMap(ODAttributeMap!, forStandardAttribute: String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODRecordMap.standardAttributeTypes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODSession.configurationForNodename(String!) -> ODConfiguration!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODSession.configurationTemplateNames

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODSession.defaultSession() -> ODSession! [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODSession.mappingTemplateNames

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified ODSession.nodeNamesAndReturnError(NSErrorPointer) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODSession.init(options: [NSObject: AnyObject]!, error: NSErrorPointer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(options inOptions: [NSObject : AnyObject]!, error outError: NSErrorPointer) ``` | OS X 10.10 |
| To | ``` init!(options inOptions: [NSObject : AnyObject]!, error outError: NSErrorPointer) ``` | OS X 10.6 |

Modified ODFrameworkErrorDomain

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ODFrameworkErrorDomain: NSString! ``` | OS X 10.10 |
| To | ``` let ODFrameworkErrorDomain: String ``` | OS X 10.6 |

Modified ODNodeAddAccountPolicy(ODNode!, CFDictionary!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeAddAccountPolicy(_ node: ODNode!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeAddAccountPolicy(_ node: ODNode!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified ODNodeCopyAccountPolicies(ODNode!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFDictionary!

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopyAccountPolicies(_ node: ODNode!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> CFDictionary! ``` |
| To | ``` func ODNodeCopyAccountPolicies(_ node: ODNode!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFDictionary! ``` |

Modified ODNodeCopyDetails(ODNode!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODNodeCopyDetails(_ node: ODNode!, _ keys: CFArray!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` | OS X 10.10 |
| To | ``` func ODNodeCopyDetails(_ node: ODNode!, _ keys: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` | OS X 10.6 |

Modified ODNodeCopyPolicies(ODNode!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>!

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func ODNodeCopyPolicies(_ node: ODNode!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` | OS X 10.10 | -- |
| To | ``` func ODNodeCopyPolicies(_ node: ODNode!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` | OS X 10.9 | OS X 10.10 |

Modified ODNodeCopyRecord(ODNode!, String!, CFString!, AnyObject!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODRecord>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODNodeCopyRecord(_ node: ODNode!, _ recordType: String!, _ recordName: CFString!, _ attributes: AnyObject!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<ODRecord>! ``` | OS X 10.10 |
| To | ``` func ODNodeCopyRecord(_ node: ODNode!, _ recordType: String!, _ recordName: CFString!, _ attributes: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODRecord>! ``` | OS X 10.6 |

Modified ODNodeCopySubnodeNames(ODNode!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODNodeCopySubnodeNames(_ node: ODNode!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` | OS X 10.10 |
| To | ``` func ODNodeCopySubnodeNames(_ node: ODNode!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` | OS X 10.6 |

Modified ODNodeCopySupportedAttributes(ODNode!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODNodeCopySupportedAttributes(_ node: ODNode!, _ recordType: String!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` | OS X 10.10 |
| To | ``` func ODNodeCopySupportedAttributes(_ node: ODNode!, _ recordType: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` | OS X 10.6 |

Modified ODNodeCopySupportedPolicies(ODNode!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>!

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func ODNodeCopySupportedPolicies(_ node: ODNode!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` | OS X 10.10 | -- |
| To | ``` func ODNodeCopySupportedPolicies(_ node: ODNode!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` | OS X 10.9 | OS X 10.10 |

Modified ODNodeCopySupportedRecordTypes(ODNode!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODNodeCopySupportedRecordTypes(_ node: ODNode!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` | OS X 10.10 |
| To | ``` func ODNodeCopySupportedRecordTypes(_ node: ODNode!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` | OS X 10.6 |

Modified ODNodeCopyUnreachableSubnodeNames(ODNode!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODNodeCopyUnreachableSubnodeNames(_ node: ODNode!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` | OS X 10.10 |
| To | ``` func ODNodeCopyUnreachableSubnodeNames(_ node: ODNode!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` | OS X 10.6 |

Modified ODNodeCreateCopy(CFAllocator!, ODNode!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNode>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODNodeCreateCopy(_ allocator: CFAllocator!, _ node: ODNode!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNode>! ``` | OS X 10.10 |
| To | ``` func ODNodeCreateCopy(_ allocator: CFAllocator!, _ node: ODNode!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNode>! ``` | OS X 10.6 |

Modified ODNodeCreateRecord(ODNode!, String!, CFString!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODRecord>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODNodeCreateRecord(_ node: ODNode!, _ recordType: String!, _ recordName: CFString!, _ attributeDict: CFDictionary!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<ODRecord>! ``` | OS X 10.10 |
| To | ``` func ODNodeCreateRecord(_ node: ODNode!, _ recordType: String!, _ recordName: CFString!, _ attributeDict: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODRecord>! ``` | OS X 10.6 |

Modified ODNodeCreateWithName(CFAllocator!, ODSession!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNode>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODNodeCreateWithName(_ allocator: CFAllocator!, _ session: ODSession!, _ nodeName: CFString!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNode>! ``` | OS X 10.10 |
| To | ``` func ODNodeCreateWithName(_ allocator: CFAllocator!, _ session: ODSession!, _ nodeName: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNode>! ``` | OS X 10.6 |

Modified ODNodeCreateWithNodeType(CFAllocator!, ODSession!, ODNodeType, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNode>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODNodeCreateWithNodeType(_ allocator: CFAllocator!, _ session: ODSession!, _ nodeType: ODNodeType, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNode>! ``` | OS X 10.10 |
| To | ``` func ODNodeCreateWithNodeType(_ allocator: CFAllocator!, _ session: ODSession!, _ nodeType: ODNodeType, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNode>! ``` | OS X 10.6 |

Modified ODNodeCustomCall(ODNode!, CFIndex, CFData!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFData!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODNodeCustomCall(_ node: ODNode!, _ customCode: CFIndex, _ data: CFData!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> CFData! ``` | OS X 10.10 |
| To | ``` func ODNodeCustomCall(_ node: ODNode!, _ customCode: CFIndex, _ data: CFData!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFData! ``` | OS X 10.6 |

Modified ODNodeCustomFunction(ODNode!, CFString!, AnyObject!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> AnyObject!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODNodeCustomFunction(_ node: ODNode!, _ function: CFString!, _ payload: AnyObject!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func ODNodeCustomFunction(_ node: ODNode!, _ function: CFString!, _ payload: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> AnyObject! ``` | OS X 10.9 |

Modified ODNodeGetName(ODNode!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODNodeGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODNodePasswordContentCheck(ODNode!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ODNodePasswordContentCheck(_ node: ODNode!, _ password: CFString!, _ recordName: CFString!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodePasswordContentCheck(_ node: ODNode!, _ password: CFString!, _ recordName: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified ODNodeRemoveAccountPolicy(ODNode!, CFDictionary!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeRemoveAccountPolicy(_ node: ODNode!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeRemoveAccountPolicy(_ node: ODNode!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified ODNodeRemovePolicy(ODNode!, ODPolicyType!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func ODNodeRemovePolicy(_ node: ODNode!, _ policyType: ODPolicyType!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 | -- |
| To | ``` func ODNodeRemovePolicy(_ node: ODNode!, _ policyType: ODPolicyType!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.9 | OS X 10.10 |

Modified ODNodeSetAccountPolicies(ODNode!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeSetAccountPolicies(_ node: ODNode!, _ policies: CFDictionary!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeSetAccountPolicies(_ node: ODNode!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified ODNodeSetCredentials(ODNode!, String!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODNodeSetCredentials(_ node: ODNode!, _ recordType: String!, _ recordName: CFString!, _ password: CFString!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func ODNodeSetCredentials(_ node: ODNode!, _ recordType: String!, _ recordName: CFString!, _ password: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.6 |

Modified ODNodeSetCredentialsExtended(ODNode!, String!, String!, CFArray!, UnsafeMutablePointer<Unmanaged<CFArray>?>, UnsafeMutablePointer<Unmanaged<ODContext>?>, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODNodeSetCredentialsExtended(_ node: ODNode!, _ recordType: String!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafePointer<Unmanaged<CFArray>?>, _ outContext: UnsafePointer<Unmanaged<ODContext>?>, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func ODNodeSetCredentialsExtended(_ node: ODNode!, _ recordType: String!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ outContext: UnsafeMutablePointer<Unmanaged<ODContext>?>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.6 |

Modified ODNodeSetPolicies(ODNode!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func ODNodeSetPolicies(_ node: ODNode!, _ policies: CFDictionary!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 | -- |
| To | ``` func ODNodeSetPolicies(_ node: ODNode!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.9 | OS X 10.10 |

Modified ODNodeSetPolicy(ODNode!, ODPolicyType!, AnyObject!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func ODNodeSetPolicy(_ node: ODNode!, _ policyType: ODPolicyType!, _ value: AnyObject!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 | -- |
| To | ``` func ODNodeSetPolicy(_ node: ODNode!, _ policyType: ODPolicyType!, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.9 | OS X 10.10 |

Modified ODPolicyType

|  | Declaration |
| --- | --- |
| From | ``` typealias ODPolicyType = CFString ``` |
| To | ``` typealias ODPolicyType = ODPolicyType ``` |

Modified ODQueryCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias ODQueryCallback = CFunctionPointer<((ODQuery!, CFArray!, CFError!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias ODQueryCallback = CFunctionPointer<((ODQuery!, CFArray!, CFError!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified ODQueryCopyResults(ODQuery!, Bool, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODQueryCopyResults(_ query: ODQuery!, _ allowPartialResults: Bool, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` | OS X 10.10 |
| To | ``` func ODQueryCopyResults(_ query: ODQuery!, _ allowPartialResults: Bool, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` | OS X 10.6 |

Modified ODQueryCreateWithNode(CFAllocator!, ODNode!, AnyObject!, String!, ODMatchType, AnyObject!, AnyObject!, CFIndex, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODQuery>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODQueryCreateWithNode(_ allocator: CFAllocator!, _ node: ODNode!, _ recordTypeOrList: AnyObject!, _ attribute: String!, _ matchType: ODMatchType, _ queryValueOrList: AnyObject!, _ returnAttributeOrList: AnyObject!, _ maxResults: CFIndex, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<ODQuery>! ``` | OS X 10.10 |
| To | ``` func ODQueryCreateWithNode(_ allocator: CFAllocator!, _ node: ODNode!, _ recordTypeOrList: AnyObject!, _ attribute: String!, _ matchType: ODMatchType, _ queryValueOrList: AnyObject!, _ returnAttributeOrList: AnyObject!, _ maxResults: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODQuery>! ``` | OS X 10.6 |

Modified ODQueryCreateWithNodeType(CFAllocator!, ODNodeType, AnyObject!, String!, ODMatchType, AnyObject!, AnyObject!, CFIndex, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODQuery>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODQueryCreateWithNodeType(_ allocator: CFAllocator!, _ nodeType: ODNodeType, _ recordTypeOrList: AnyObject!, _ attribute: String!, _ matchType: ODMatchType, _ queryValueOrList: AnyObject!, _ returnAttributeOrList: AnyObject!, _ maxResults: CFIndex, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<ODQuery>! ``` | OS X 10.10 |
| To | ``` func ODQueryCreateWithNodeType(_ allocator: CFAllocator!, _ nodeType: ODNodeType, _ recordTypeOrList: AnyObject!, _ attribute: String!, _ matchType: ODMatchType, _ queryValueOrList: AnyObject!, _ returnAttributeOrList: AnyObject!, _ maxResults: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODQuery>! ``` | OS X 10.6 |

Modified ODQueryGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODQueryScheduleWithRunLoop(ODQuery!, CFRunLoop!, CFString!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODQuerySetCallback(ODQuery!, ODQueryCallback, UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODQuerySetCallback(_ query: ODQuery!, _ callback: ODQueryCallback, _ userInfo: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func ODQuerySetCallback(_ query: ODQuery!, _ callback: ODQueryCallback, _ userInfo: UnsafeMutablePointer<Void>) ``` | OS X 10.6 |

Modified ODQuerySetDispatchQueue(ODQuery!, dispatch_queue_t!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODQuerySynchronize(ODQuery!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODQueryUnscheduleFromRunLoop(ODQuery!, CFRunLoop!, CFString!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecordAddAccountPolicy(ODRecord!, CFDictionary!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordAddAccountPolicy(_ record: ODRecord!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordAddAccountPolicy(_ record: ODRecord!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified ODRecordAddMember(ODRecord!, ODRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODRecordAddMember(_ group: ODRecord!, _ member: ODRecord!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func ODRecordAddMember(_ group: ODRecord!, _ member: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.6 |

Modified ODRecordAddValue(ODRecord!, String!, AnyObject!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODRecordAddValue(_ record: ODRecord!, _ attribute: String!, _ value: AnyObject!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func ODRecordAddValue(_ record: ODRecord!, _ attribute: String!, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.6 |

Modified ODRecordAuthenticationAllowed(ODRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordAuthenticationAllowed(_ record: ODRecord!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordAuthenticationAllowed(_ record: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified ODRecordChangePassword(ODRecord!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODRecordChangePassword(_ record: ODRecord!, _ oldPassword: CFString!, _ newPassword: CFString!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func ODRecordChangePassword(_ record: ODRecord!, _ oldPassword: CFString!, _ newPassword: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.6 |

Modified ODRecordContainsMember(ODRecord!, ODRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODRecordContainsMember(_ group: ODRecord!, _ member: ODRecord!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func ODRecordContainsMember(_ group: ODRecord!, _ member: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.6 |

Modified ODRecordCopyAccountPolicies(ODRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFDictionary!

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordCopyAccountPolicies(_ record: ODRecord!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> CFDictionary! ``` |
| To | ``` func ODRecordCopyAccountPolicies(_ record: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFDictionary! ``` |

Modified ODRecordCopyDetails(ODRecord!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODRecordCopyDetails(_ record: ODRecord!, _ attributes: CFArray!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` | OS X 10.10 |
| To | ``` func ODRecordCopyDetails(_ record: ODRecord!, _ attributes: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` | OS X 10.6 |

Modified ODRecordCopyEffectivePolicies(ODRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>!

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func ODRecordCopyEffectivePolicies(_ record: ODRecord!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` | OS X 10.10 | -- |
| To | ``` func ODRecordCopyEffectivePolicies(_ record: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` | OS X 10.9 | OS X 10.10 |

Modified ODRecordCopyPolicies(ODRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>!

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func ODRecordCopyPolicies(_ record: ODRecord!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` | OS X 10.10 | -- |
| To | ``` func ODRecordCopyPolicies(_ record: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` | OS X 10.9 | OS X 10.10 |

Modified ODRecordCopySupportedPolicies(ODRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>!

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func ODRecordCopySupportedPolicies(_ record: ODRecord!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` | OS X 10.10 | -- |
| To | ``` func ODRecordCopySupportedPolicies(_ record: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` | OS X 10.9 | OS X 10.10 |

Modified ODRecordCopyValues(ODRecord!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODRecordCopyValues(_ record: ODRecord!, _ attribute: String!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` | OS X 10.10 |
| To | ``` func ODRecordCopyValues(_ record: ODRecord!, _ attribute: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` | OS X 10.6 |

Modified ODRecordDelete(ODRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODRecordDelete(_ record: ODRecord!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func ODRecordDelete(_ record: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.6 |

Modified ODRecordGetRecordName(ODRecord!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecordGetRecordType(ODRecord!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecordGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODRecordPasswordChangeAllowed(ODRecord!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordPasswordChangeAllowed(_ record: ODRecord!, _ newPassword: CFString!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordPasswordChangeAllowed(_ record: ODRecord!, _ newPassword: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified ODRecordRemoveAccountPolicy(ODRecord!, CFDictionary!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordRemoveAccountPolicy(_ record: ODRecord!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordRemoveAccountPolicy(_ record: ODRecord!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified ODRecordRemoveMember(ODRecord!, ODRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODRecordRemoveMember(_ group: ODRecord!, _ member: ODRecord!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func ODRecordRemoveMember(_ group: ODRecord!, _ member: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.6 |

Modified ODRecordRemovePolicy(ODRecord!, ODPolicyType!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func ODRecordRemovePolicy(_ record: ODRecord!, _ policy: ODPolicyType!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 | -- |
| To | ``` func ODRecordRemovePolicy(_ record: ODRecord!, _ policy: ODPolicyType!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.9 | OS X 10.10 |

Modified ODRecordRemoveValue(ODRecord!, String!, AnyObject!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODRecordRemoveValue(_ record: ODRecord!, _ attribute: String!, _ value: AnyObject!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func ODRecordRemoveValue(_ record: ODRecord!, _ attribute: String!, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.6 |

Modified ODRecordSetAccountPolicies(ODRecord!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordSetAccountPolicies(_ record: ODRecord!, _ policies: CFDictionary!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordSetAccountPolicies(_ record: ODRecord!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified ODRecordSetNodeCredentials(ODRecord!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODRecordSetNodeCredentials(_ record: ODRecord!, _ username: CFString!, _ password: CFString!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func ODRecordSetNodeCredentials(_ record: ODRecord!, _ username: CFString!, _ password: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.6 |

Modified ODRecordSetNodeCredentialsExtended(ODRecord!, String!, String!, CFArray!, UnsafeMutablePointer<Unmanaged<CFArray>?>, UnsafeMutablePointer<Unmanaged<ODContext>?>, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODRecordSetNodeCredentialsExtended(_ record: ODRecord!, _ recordType: String!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafePointer<Unmanaged<CFArray>?>, _ outContext: UnsafePointer<Unmanaged<ODContext>?>, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func ODRecordSetNodeCredentialsExtended(_ record: ODRecord!, _ recordType: String!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ outContext: UnsafeMutablePointer<Unmanaged<ODContext>?>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.6 |

Modified ODRecordSetPolicies(ODRecord!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func ODRecordSetPolicies(_ record: ODRecord!, _ policies: CFDictionary!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 | -- |
| To | ``` func ODRecordSetPolicies(_ record: ODRecord!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.9 | OS X 10.10 |

Modified ODRecordSetPolicy(ODRecord!, ODPolicyType!, AnyObject!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func ODRecordSetPolicy(_ record: ODRecord!, _ policy: ODPolicyType!, _ value: AnyObject!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 | -- |
| To | ``` func ODRecordSetPolicy(_ record: ODRecord!, _ policy: ODPolicyType!, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.9 | OS X 10.10 |

Modified ODRecordSetValue(ODRecord!, String!, AnyObject!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODRecordSetValue(_ record: ODRecord!, _ attribute: String!, _ valueOrValues: AnyObject!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func ODRecordSetValue(_ record: ODRecord!, _ attribute: String!, _ valueOrValues: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.6 |

Modified ODRecordSynchronize(ODRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODRecordSynchronize(_ record: ODRecord!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func ODRecordSynchronize(_ record: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.6 |

Modified ODRecordVerifyPassword(ODRecord!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODRecordVerifyPassword(_ record: ODRecord!, _ password: CFString!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func ODRecordVerifyPassword(_ record: ODRecord!, _ password: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.6 |

Modified ODRecordVerifyPasswordExtended(ODRecord!, String!, CFArray!, UnsafeMutablePointer<Unmanaged<CFArray>?>, UnsafeMutablePointer<Unmanaged<ODContext>?>, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODRecordVerifyPasswordExtended(_ record: ODRecord!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafePointer<Unmanaged<CFArray>?>, _ outContext: UnsafePointer<Unmanaged<ODContext>?>, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func ODRecordVerifyPasswordExtended(_ record: ODRecord!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ outContext: UnsafeMutablePointer<Unmanaged<ODContext>?>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.6 |

Modified ODSessionCopyNodeNames(CFAllocator!, ODSession!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODSessionCopyNodeNames(_ allocator: CFAllocator!, _ session: ODSession!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` | OS X 10.10 |
| To | ``` func ODSessionCopyNodeNames(_ allocator: CFAllocator!, _ session: ODSession!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` | OS X 10.6 |

Modified ODSessionCreate(CFAllocator!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODSession>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ODSessionCreate(_ allocator: CFAllocator!, _ options: CFDictionary!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<ODSession>! ``` | OS X 10.10 |
| To | ``` func ODSessionCreate(_ allocator: CFAllocator!, _ options: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODSession>! ``` | OS X 10.6 |

Modified ODSessionGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified ODSessionProxyAddress

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ODSessionProxyAddress: NSString! ``` | OS X 10.10 |
| To | ``` let ODSessionProxyAddress: String ``` | OS X 10.6 |

Modified ODSessionProxyPassword

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ODSessionProxyPassword: NSString! ``` | OS X 10.10 |
| To | ``` let ODSessionProxyPassword: String ``` | OS X 10.6 |

Modified ODSessionProxyPort

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ODSessionProxyPort: NSString! ``` | OS X 10.10 |
| To | ``` let ODSessionProxyPort: String ``` | OS X 10.6 |

Modified ODSessionProxyUsername

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ODSessionProxyUsername: NSString! ``` | OS X 10.10 |
| To | ``` let ODSessionProxyUsername: String ``` | OS X 10.6 |

Modified ODTrustTypeAnonymous

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ODTrustTypeAnonymous: NSString! ``` | OS X 10.10 |
| To | ``` let ODTrustTypeAnonymous: String ``` | OS X 10.9 |

Modified ODTrustTypeJoined

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ODTrustTypeJoined: NSString! ``` | OS X 10.10 |
| To | ``` let ODTrustTypeJoined: String ``` | OS X 10.9 |

Modified ODTrustTypeUsingCredentials

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ODTrustTypeUsingCredentials: NSString! ``` | OS X 10.10 |
| To | ``` let ODTrustTypeUsingCredentials: String ``` | OS X 10.9 |

Modified kODAttributeTypeAccessControlEntry

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAccessControlEntry: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAccessControlEntry: String ``` |

Modified kODAttributeTypeAddressLine1

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAddressLine1: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAddressLine1: String ``` |

Modified kODAttributeTypeAddressLine2

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAddressLine2: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAddressLine2: String ``` |

Modified kODAttributeTypeAddressLine3

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAddressLine3: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAddressLine3: String ``` |

Modified kODAttributeTypeAdminLimits

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAdminLimits: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAdminLimits: String ``` |

Modified kODAttributeTypeAdvertisedServices

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kODAttributeTypeAdvertisedServices: ODAttributeType! ``` | OS X 10.10 |
| To | ``` let kODAttributeTypeAdvertisedServices: String ``` | OS X 10.7 |

Modified kODAttributeTypeAlias

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAlias: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAlias: String ``` |

Modified kODAttributeTypeAllAttributes

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAllAttributes: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAllAttributes: String ``` |

Modified kODAttributeTypeAllTypes

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAllTypes: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAllTypes: String ``` |

Modified kODAttributeTypeAltSecurityIdentities

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kODAttributeTypeAltSecurityIdentities: ODAttributeType! ``` | OS X 10.10 |
| To | ``` let kODAttributeTypeAltSecurityIdentities: String ``` | OS X 10.6 |

Modified kODAttributeTypeAreaCode

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAreaCode: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAreaCode: String ``` |

Modified kODAttributeTypeAttrListRefCount

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAttrListRefCount: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAttrListRefCount: String ``` |

Modified kODAttributeTypeAttrListRefs

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAttrListRefs: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAttrListRefs: String ``` |

Modified kODAttributeTypeAttrListValueRefCount

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAttrListValueRefCount: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAttrListValueRefCount: String ``` |

Modified kODAttributeTypeAttrListValueRefs

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAttrListValueRefs: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAttrListValueRefs: String ``` |

Modified kODAttributeTypeAuthCredential

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAuthCredential: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAuthCredential: String ``` |

Modified kODAttributeTypeAuthMethod

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAuthMethod: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAuthMethod: String ``` |

Modified kODAttributeTypeAuthenticationAuthority

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAuthenticationAuthority: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAuthenticationAuthority: String ``` |

Modified kODAttributeTypeAuthenticationHint

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAuthenticationHint: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAuthenticationHint: String ``` |

Modified kODAttributeTypeAuthorityRevocationList

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAuthorityRevocationList: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAuthorityRevocationList: String ``` |

Modified kODAttributeTypeAutomaticSearchPath

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAutomaticSearchPath: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAutomaticSearchPath: String ``` |

Modified kODAttributeTypeAutomountInformation

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeAutomountInformation: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeAutomountInformation: String ``` |

Modified kODAttributeTypeBirthday

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeBirthday: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeBirthday: String ``` |

Modified kODAttributeTypeBootParams

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeBootParams: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeBootParams: String ``` |

Modified kODAttributeTypeBuildVersion

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeBuildVersion: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeBuildVersion: String ``` |

Modified kODAttributeTypeBuilding

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeBuilding: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeBuilding: String ``` |

Modified kODAttributeTypeCACertificate

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeCACertificate: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeCACertificate: String ``` |

Modified kODAttributeTypeCapacity

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeCapacity: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeCapacity: String ``` |

Modified kODAttributeTypeCertificateRevocationList

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeCertificateRevocationList: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeCertificateRevocationList: String ``` |

Modified kODAttributeTypeCity

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeCity: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeCity: String ``` |

Modified kODAttributeTypeComment

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeComment: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeComment: String ``` |

Modified kODAttributeTypeCompany

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeCompany: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeCompany: String ``` |

Modified kODAttributeTypeComputers

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeComputers: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeComputers: String ``` |

Modified kODAttributeTypeConfigAvailable

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeConfigAvailable: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeConfigAvailable: String ``` |

Modified kODAttributeTypeConfigFile

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeConfigFile: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeConfigFile: String ``` |

Modified kODAttributeTypeContactGUID

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeContactGUID: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeContactGUID: String ``` |

Modified kODAttributeTypeContactPerson

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeContactPerson: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeContactPerson: String ``` |

Modified kODAttributeTypeCopyTimestamp

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeCopyTimestamp: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeCopyTimestamp: String ``` |

Modified kODAttributeTypeCoreFWVersion

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeCoreFWVersion: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeCoreFWVersion: String ``` |

Modified kODAttributeTypeCountry

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeCountry: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeCountry: String ``` |

Modified kODAttributeTypeCreationTimestamp

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeCreationTimestamp: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeCreationTimestamp: String ``` |

Modified kODAttributeTypeCrossCertificatePair

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeCrossCertificatePair: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeCrossCertificatePair: String ``` |

Modified kODAttributeTypeCustomSearchPath

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeCustomSearchPath: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeCustomSearchPath: String ``` |

Modified kODAttributeTypeDNSDomain

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeDNSDomain: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeDNSDomain: String ``` |

Modified kODAttributeTypeDNSName

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeDNSName: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeDNSName: String ``` |

Modified kODAttributeTypeDNSNameServer

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeDNSNameServer: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeDNSNameServer: String ``` |

Modified kODAttributeTypeDataStamp

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeDataStamp: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeDataStamp: String ``` |

Modified kODAttributeTypeDateRecordCreated

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeDateRecordCreated: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeDateRecordCreated: String ``` |

Modified kODAttributeTypeDepartment

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeDepartment: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeDepartment: String ``` |

Modified kODAttributeTypeDirRefCount

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeDirRefCount: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeDirRefCount: String ``` |

Modified kODAttributeTypeDirRefs

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeDirRefs: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeDirRefs: String ``` |

Modified kODAttributeTypeEMailAddress

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeEMailAddress: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeEMailAddress: String ``` |

Modified kODAttributeTypeEMailContacts

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeEMailContacts: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeEMailContacts: String ``` |

Modified kODAttributeTypeENetAddress

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeENetAddress: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeENetAddress: String ``` |

Modified kODAttributeTypeExpire

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeExpire: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeExpire: String ``` |

Modified kODAttributeTypeFWVersion

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeFWVersion: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeFWVersion: String ``` |

Modified kODAttributeTypeFaxNumber

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeFaxNumber: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeFaxNumber: String ``` |

Modified kODAttributeTypeFirstName

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeFirstName: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeFirstName: String ``` |

Modified kODAttributeTypeFullName

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeFullName: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeFullName: String ``` |

Modified kODAttributeTypeFunctionalState

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeFunctionalState: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeFunctionalState: String ``` |

Modified kODAttributeTypeGUID

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeGUID: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeGUID: String ``` |

Modified kODAttributeTypeGroup

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeGroup: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeGroup: String ``` |

Modified kODAttributeTypeGroupMembers

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeGroupMembers: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeGroupMembers: String ``` |

Modified kODAttributeTypeGroupMembership

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeGroupMembership: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeGroupMembership: String ``` |

Modified kODAttributeTypeGroupServices

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeGroupServices: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeGroupServices: String ``` |

Modified kODAttributeTypeHTML

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeHTML: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeHTML: String ``` |

Modified kODAttributeTypeHardwareUUID

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kODAttributeTypeHardwareUUID: ODAttributeType! ``` | OS X 10.10 |
| To | ``` let kODAttributeTypeHardwareUUID: String ``` | OS X 10.6 |

Modified kODAttributeTypeHomeDirectory

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeHomeDirectory: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeHomeDirectory: String ``` |

Modified kODAttributeTypeHomeDirectoryQuota

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeHomeDirectoryQuota: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeHomeDirectoryQuota: String ``` |

Modified kODAttributeTypeHomeDirectorySoftQuota

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeHomeDirectorySoftQuota: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeHomeDirectorySoftQuota: String ``` |

Modified kODAttributeTypeHomeLocOwner

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeHomeLocOwner: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeHomeLocOwner: String ``` |

Modified kODAttributeTypeHomePhoneNumber

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeHomePhoneNumber: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeHomePhoneNumber: String ``` |

Modified kODAttributeTypeIMHandle

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeIMHandle: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeIMHandle: String ``` |

Modified kODAttributeTypeIPAddress

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeIPAddress: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeIPAddress: String ``` |

Modified kODAttributeTypeIPAddressAndENetAddress

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeIPAddressAndENetAddress: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeIPAddressAndENetAddress: String ``` |

Modified kODAttributeTypeIPv6Address

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeIPv6Address: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeIPv6Address: String ``` |

Modified kODAttributeTypeInternetAlias

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeInternetAlias: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeInternetAlias: String ``` |

Modified kODAttributeTypeJPEGPhoto

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeJPEGPhoto: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeJPEGPhoto: String ``` |

Modified kODAttributeTypeJobTitle

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeJobTitle: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeJobTitle: String ``` |

Modified kODAttributeTypeKDCAuthKey

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeKDCAuthKey: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeKDCAuthKey: String ``` |

Modified kODAttributeTypeKDCConfigData

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeKDCConfigData: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeKDCConfigData: String ``` |

Modified kODAttributeTypeKerberosRealm

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeKerberosRealm: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeKerberosRealm: String ``` |

Modified kODAttributeTypeKerberosServices

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kODAttributeTypeKerberosServices: ODAttributeType! ``` | OS X 10.10 |
| To | ``` let kODAttributeTypeKerberosServices: String ``` | OS X 10.7 |

Modified kODAttributeTypeKeywords

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeKeywords: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeKeywords: String ``` |

Modified kODAttributeTypeLDAPReadReplicas

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeLDAPReadReplicas: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeLDAPReadReplicas: String ``` |

Modified kODAttributeTypeLDAPSearchBaseSuffix

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeLDAPSearchBaseSuffix: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeLDAPSearchBaseSuffix: String ``` |

Modified kODAttributeTypeLDAPWriteReplicas

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeLDAPWriteReplicas: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeLDAPWriteReplicas: String ``` |

Modified kODAttributeTypeLastName

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeLastName: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeLastName: String ``` |

Modified kODAttributeTypeLocalOnlySearchPath

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeLocalOnlySearchPath: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeLocalOnlySearchPath: String ``` |

Modified kODAttributeTypeLocaleRelay

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kODAttributeTypeLocaleRelay: ODAttributeType! ``` | OS X 10.10 |
| To | ``` let kODAttributeTypeLocaleRelay: String ``` | OS X 10.7 |

Modified kODAttributeTypeLocaleSubnets

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kODAttributeTypeLocaleSubnets: ODAttributeType! ``` | OS X 10.10 |
| To | ``` let kODAttributeTypeLocaleSubnets: String ``` | OS X 10.7 |

Modified kODAttributeTypeLocation

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeLocation: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeLocation: String ``` |

Modified kODAttributeTypeMCXFlags

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeMCXFlags: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeMCXFlags: String ``` |

Modified kODAttributeTypeMCXSettings

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeMCXSettings: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeMCXSettings: String ``` |

Modified kODAttributeTypeMIME

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeMIME: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeMIME: String ``` |

Modified kODAttributeTypeMailAttribute

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeMailAttribute: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeMailAttribute: String ``` |

Modified kODAttributeTypeMapCoordinates

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeMapCoordinates: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeMapCoordinates: String ``` |

Modified kODAttributeTypeMapGUID

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeMapGUID: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeMapGUID: String ``` |

Modified kODAttributeTypeMapURI

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeMapURI: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeMapURI: String ``` |

Modified kODAttributeTypeMetaAmbiguousName

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeMetaAmbiguousName: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeMetaAmbiguousName: String ``` |

Modified kODAttributeTypeMetaAugmentedAttributes

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeMetaAugmentedAttributes: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeMetaAugmentedAttributes: String ``` |

Modified kODAttributeTypeMetaAutomountMap

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeMetaAutomountMap: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeMetaAutomountMap: String ``` |

Modified kODAttributeTypeMetaNodeLocation

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeMetaNodeLocation: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeMetaNodeLocation: String ``` |

Modified kODAttributeTypeMetaRecordName

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeMetaRecordName: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeMetaRecordName: String ``` |

Modified kODAttributeTypeMiddleName

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeMiddleName: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeMiddleName: String ``` |

Modified kODAttributeTypeMobileNumber

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeMobileNumber: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeMobileNumber: String ``` |

Modified kODAttributeTypeModificationTimestamp

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeModificationTimestamp: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeModificationTimestamp: String ``` |

Modified kODAttributeTypeNFSHomeDirectory

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeNFSHomeDirectory: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeNFSHomeDirectory: String ``` |

Modified kODAttributeTypeNTDomainComputerAccount

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeNTDomainComputerAccount: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeNTDomainComputerAccount: String ``` |

Modified kODAttributeTypeNamePrefix

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeNamePrefix: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeNamePrefix: String ``` |

Modified kODAttributeTypeNameSuffix

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeNameSuffix: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeNameSuffix: String ``` |

Modified kODAttributeTypeNativeOnly

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeNativeOnly: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeNativeOnly: String ``` |

Modified kODAttributeTypeNestedGroups

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeNestedGroups: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeNestedGroups: String ``` |

Modified kODAttributeTypeNetGroupTriplet

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeNetGroupTriplet: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeNetGroupTriplet: String ``` |

Modified kODAttributeTypeNetGroups

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeNetGroups: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeNetGroups: String ``` |

Modified kODAttributeTypeNetworkInterfaces

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kODAttributeTypeNetworkInterfaces: ODAttributeType! ``` | OS X 10.10 |
| To | ``` let kODAttributeTypeNetworkInterfaces: String ``` | OS X 10.7 |

Modified kODAttributeTypeNetworkNumber

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeNetworkNumber: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeNetworkNumber: String ``` |

Modified kODAttributeTypeNickName

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeNickName: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeNickName: String ``` |

Modified kODAttributeTypeNodeOptions

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kODAttributeTypeNodeOptions: ODAttributeType! ``` | OS X 10.10 |
| To | ``` let kODAttributeTypeNodeOptions: String ``` | OS X 10.7 |

Modified kODAttributeTypeNodePath

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeNodePath: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeNodePath: String ``` |

Modified kODAttributeTypeNodeRefCount

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeNodeRefCount: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeNodeRefCount: String ``` |

Modified kODAttributeTypeNodeRefs

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeNodeRefs: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeNodeRefs: String ``` |

Modified kODAttributeTypeNodeSASLRealm

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kODAttributeTypeNodeSASLRealm: ODAttributeType! ``` | OS X 10.10 |
| To | ``` let kODAttributeTypeNodeSASLRealm: String ``` | OS X 10.9 |

Modified kODAttributeTypeNote

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeNote: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeNote: String ``` |

Modified kODAttributeTypeNumTableList

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeNumTableList: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeNumTableList: String ``` |

Modified kODAttributeTypeOperatingSystem

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kODAttributeTypeOperatingSystem: ODAttributeType! ``` | OS X 10.10 |
| To | ``` let kODAttributeTypeOperatingSystem: String ``` | OS X 10.6 |

Modified kODAttributeTypeOperatingSystemVersion

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kODAttributeTypeOperatingSystemVersion: ODAttributeType! ``` | OS X 10.10 |
| To | ``` let kODAttributeTypeOperatingSystemVersion: String ``` | OS X 10.6 |

Modified kODAttributeTypeOrganizationInfo

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeOrganizationInfo: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeOrganizationInfo: String ``` |

Modified kODAttributeTypeOrganizationName

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeOrganizationName: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeOrganizationName: String ``` |

Modified kODAttributeTypeOriginalHomeDirectory

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeOriginalHomeDirectory: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeOriginalHomeDirectory: String ``` |

Modified kODAttributeTypeOriginalNFSHomeDirectory

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeOriginalNFSHomeDirectory: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeOriginalNFSHomeDirectory: String ``` |

Modified kODAttributeTypeOriginalNodeName

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeOriginalNodeName: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeOriginalNodeName: String ``` |

Modified kODAttributeTypeOwner

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeOwner: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeOwner: String ``` |

Modified kODAttributeTypeOwnerGUID

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeOwnerGUID: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeOwnerGUID: String ``` |

Modified kODAttributeTypePGPPublicKey

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePGPPublicKey: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePGPPublicKey: String ``` |

Modified kODAttributeTypePIDValue

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePIDValue: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePIDValue: String ``` |

Modified kODAttributeTypePagerNumber

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePagerNumber: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePagerNumber: String ``` |

Modified kODAttributeTypeParentLocales

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kODAttributeTypeParentLocales: ODAttributeType! ``` | OS X 10.10 |
| To | ``` let kODAttributeTypeParentLocales: String ``` | OS X 10.7 |

Modified kODAttributeTypePassword

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePassword: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePassword: String ``` |

Modified kODAttributeTypePasswordPlus

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePasswordPlus: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePasswordPlus: String ``` |

Modified kODAttributeTypePasswordPolicyOptions

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePasswordPolicyOptions: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePasswordPolicyOptions: String ``` |

Modified kODAttributeTypePasswordServerList

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePasswordServerList: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePasswordServerList: String ``` |

Modified kODAttributeTypePasswordServerLocation

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePasswordServerLocation: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePasswordServerLocation: String ``` |

Modified kODAttributeTypePhoneContacts

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePhoneContacts: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePhoneContacts: String ``` |

Modified kODAttributeTypePhoneNumber

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePhoneNumber: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePhoneNumber: String ``` |

Modified kODAttributeTypePicture

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePicture: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePicture: String ``` |

Modified kODAttributeTypePlugInInfo

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePlugInInfo: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePlugInInfo: String ``` |

Modified kODAttributeTypePluginIndex

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePluginIndex: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePluginIndex: String ``` |

Modified kODAttributeTypePort

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePort: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePort: String ``` |

Modified kODAttributeTypePostalAddress

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePostalAddress: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePostalAddress: String ``` |

Modified kODAttributeTypePostalAddressContacts

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePostalAddressContacts: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePostalAddressContacts: String ``` |

Modified kODAttributeTypePostalCode

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePostalCode: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePostalCode: String ``` |

Modified kODAttributeTypePresetUserIsAdmin

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePresetUserIsAdmin: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePresetUserIsAdmin: String ``` |

Modified kODAttributeTypePrimaryComputerGUID

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePrimaryComputerGUID: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePrimaryComputerGUID: String ``` |

Modified kODAttributeTypePrimaryComputerList

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePrimaryComputerList: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePrimaryComputerList: String ``` |

Modified kODAttributeTypePrimaryGroupID

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePrimaryGroupID: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePrimaryGroupID: String ``` |

Modified kODAttributeTypePrimaryLocale

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kODAttributeTypePrimaryLocale: ODAttributeType! ``` | OS X 10.10 |
| To | ``` let kODAttributeTypePrimaryLocale: String ``` | OS X 10.7 |

Modified kODAttributeTypePrimaryNTDomain

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePrimaryNTDomain: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePrimaryNTDomain: String ``` |

Modified kODAttributeTypePrintServiceInfoText

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePrintServiceInfoText: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePrintServiceInfoText: String ``` |

Modified kODAttributeTypePrintServiceInfoXML

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePrintServiceInfoXML: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePrintServiceInfoXML: String ``` |

Modified kODAttributeTypePrintServiceUserData

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePrintServiceUserData: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePrintServiceUserData: String ``` |

Modified kODAttributeTypePrinter1284DeviceID

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePrinter1284DeviceID: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePrinter1284DeviceID: String ``` |

Modified kODAttributeTypePrinterLPRHost

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePrinterLPRHost: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePrinterLPRHost: String ``` |

Modified kODAttributeTypePrinterLPRQueue

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePrinterLPRQueue: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePrinterLPRQueue: String ``` |

Modified kODAttributeTypePrinterMakeAndModel

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePrinterMakeAndModel: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePrinterMakeAndModel: String ``` |

Modified kODAttributeTypePrinterType

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePrinterType: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePrinterType: String ``` |

Modified kODAttributeTypePrinterURI

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePrinterURI: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePrinterURI: String ``` |

Modified kODAttributeTypePrinterXRISupported

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePrinterXRISupported: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePrinterXRISupported: String ``` |

Modified kODAttributeTypeProcessName

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeProcessName: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeProcessName: String ``` |

Modified kODAttributeTypeProfiles

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kODAttributeTypeProfiles: ODAttributeType! ``` | OS X 10.10 |
| To | ``` let kODAttributeTypeProfiles: String ``` | OS X 10.9 |

Modified kODAttributeTypeProfilesTimestamp

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kODAttributeTypeProfilesTimestamp: ODAttributeType! ``` | OS X 10.10 |
| To | ``` let kODAttributeTypeProfilesTimestamp: String ``` | OS X 10.9 |

Modified kODAttributeTypeProtocolNumber

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeProtocolNumber: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeProtocolNumber: String ``` |

Modified kODAttributeTypeProtocols

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeProtocols: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeProtocols: String ``` |

Modified kODAttributeTypePwdAgingPolicy

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypePwdAgingPolicy: ODAttributeType! ``` |
| To | ``` let kODAttributeTypePwdAgingPolicy: String ``` |

Modified kODAttributeTypeRPCNumber

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeRPCNumber: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeRPCNumber: String ``` |

Modified kODAttributeTypeReadOnlyNode

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeReadOnlyNode: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeReadOnlyNode: String ``` |

Modified kODAttributeTypeRealUserID

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeRealUserID: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeRealUserID: String ``` |

Modified kODAttributeTypeRecRefCount

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeRecRefCount: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeRecRefCount: String ``` |

Modified kODAttributeTypeRecRefs

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeRecRefs: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeRecRefs: String ``` |

Modified kODAttributeTypeRecordName

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeRecordName: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeRecordName: String ``` |

Modified kODAttributeTypeRecordType

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeRecordType: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeRecordType: String ``` |

Modified kODAttributeTypeRelationships

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeRelationships: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeRelationships: String ``` |

Modified kODAttributeTypeRelativeDNPrefix

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeRelativeDNPrefix: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeRelativeDNPrefix: String ``` |

Modified kODAttributeTypeResourceInfo

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeResourceInfo: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeResourceInfo: String ``` |

Modified kODAttributeTypeResourceType

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeResourceType: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeResourceType: String ``` |

Modified kODAttributeTypeSMBAcctFlags

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSMBAcctFlags: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSMBAcctFlags: String ``` |

Modified kODAttributeTypeSMBGroupRID

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSMBGroupRID: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSMBGroupRID: String ``` |

Modified kODAttributeTypeSMBHome

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSMBHome: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSMBHome: String ``` |

Modified kODAttributeTypeSMBHomeDrive

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSMBHomeDrive: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSMBHomeDrive: String ``` |

Modified kODAttributeTypeSMBKickoffTime

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSMBKickoffTime: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSMBKickoffTime: String ``` |

Modified kODAttributeTypeSMBLogoffTime

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSMBLogoffTime: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSMBLogoffTime: String ``` |

Modified kODAttributeTypeSMBLogonTime

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSMBLogonTime: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSMBLogonTime: String ``` |

Modified kODAttributeTypeSMBPWDLastSet

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSMBPWDLastSet: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSMBPWDLastSet: String ``` |

Modified kODAttributeTypeSMBPrimaryGroupSID

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSMBPrimaryGroupSID: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSMBPrimaryGroupSID: String ``` |

Modified kODAttributeTypeSMBProfilePath

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSMBProfilePath: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSMBProfilePath: String ``` |

Modified kODAttributeTypeSMBRID

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSMBRID: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSMBRID: String ``` |

Modified kODAttributeTypeSMBSID

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSMBSID: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSMBSID: String ``` |

Modified kODAttributeTypeSMBScriptPath

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSMBScriptPath: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSMBScriptPath: String ``` |

Modified kODAttributeTypeSMBUserWorkstations

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSMBUserWorkstations: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSMBUserWorkstations: String ``` |

Modified kODAttributeTypeSchema

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSchema: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSchema: String ``` |

Modified kODAttributeTypeSearchPath

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSearchPath: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSearchPath: String ``` |

Modified kODAttributeTypeSearchPolicy

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSearchPolicy: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSearchPolicy: String ``` |

Modified kODAttributeTypeServiceType

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeServiceType: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeServiceType: String ``` |

Modified kODAttributeTypeServicesLocator

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeServicesLocator: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeServicesLocator: String ``` |

Modified kODAttributeTypeSetupAdvertising

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSetupAdvertising: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSetupAdvertising: String ``` |

Modified kODAttributeTypeSetupAutoRegister

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSetupAutoRegister: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSetupAutoRegister: String ``` |

Modified kODAttributeTypeSetupLocation

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSetupLocation: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSetupLocation: String ``` |

Modified kODAttributeTypeSetupOccupation

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSetupOccupation: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSetupOccupation: String ``` |

Modified kODAttributeTypeStandardOnly

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeStandardOnly: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeStandardOnly: String ``` |

Modified kODAttributeTypeState

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeState: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeState: String ``` |

Modified kODAttributeTypeStreet

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeStreet: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeStreet: String ``` |

Modified kODAttributeTypeSubNodes

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeSubNodes: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeSubNodes: String ``` |

Modified kODAttributeTypeTimePackage

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeTimePackage: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeTimePackage: String ``` |

Modified kODAttributeTypeTimeToLive

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeTimeToLive: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeTimeToLive: String ``` |

Modified kODAttributeTypeTotalRefCount

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeTotalRefCount: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeTotalRefCount: String ``` |

Modified kODAttributeTypeTotalSize

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeTotalSize: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeTotalSize: String ``` |

Modified kODAttributeTypeTrustInformation

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeTrustInformation: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeTrustInformation: String ``` |

Modified kODAttributeTypeURL

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeURL: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeURL: String ``` |

Modified kODAttributeTypeUniqueID

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeUniqueID: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeUniqueID: String ``` |

Modified kODAttributeTypeUserCertificate

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeUserCertificate: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeUserCertificate: String ``` |

Modified kODAttributeTypeUserPKCS12Data

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeUserPKCS12Data: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeUserPKCS12Data: String ``` |

Modified kODAttributeTypeUserSMIMECertificate

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeUserSMIMECertificate: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeUserSMIMECertificate: String ``` |

Modified kODAttributeTypeUserShell

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeUserShell: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeUserShell: String ``` |

Modified kODAttributeTypeVFSDumpFreq

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeVFSDumpFreq: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeVFSDumpFreq: String ``` |

Modified kODAttributeTypeVFSLinkDir

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeVFSLinkDir: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeVFSLinkDir: String ``` |

Modified kODAttributeTypeVFSOpts

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeVFSOpts: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeVFSOpts: String ``` |

Modified kODAttributeTypeVFSPassNo

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeVFSPassNo: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeVFSPassNo: String ``` |

Modified kODAttributeTypeVFSType

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeVFSType: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeVFSType: String ``` |

Modified kODAttributeTypeVersion

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeVersion: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeVersion: String ``` |

Modified kODAttributeTypeWeblogURI

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeWeblogURI: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeWeblogURI: String ``` |

Modified kODAttributeTypeXMLPlist

|  | Declaration |
| --- | --- |
| From | ``` let kODAttributeTypeXMLPlist: ODAttributeType! ``` |
| To | ``` let kODAttributeTypeXMLPlist: String ``` |

Modified kODAuthenticationType2WayRandom

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationType2WayRandom: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationType2WayRandom: String ``` |

Modified kODAuthenticationType2WayRandomChangePasswd

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationType2WayRandomChangePasswd: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationType2WayRandomChangePasswd: String ``` |

Modified kODAuthenticationTypeAPOP

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeAPOP: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeAPOP: String ``` |

Modified kODAuthenticationTypeCRAM_MD5

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeCRAM_MD5: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeCRAM_MD5: String ``` |

Modified kODAuthenticationTypeChangePasswd

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeChangePasswd: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeChangePasswd: String ``` |

Modified kODAuthenticationTypeClearText

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeClearText: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeClearText: String ``` |

Modified kODAuthenticationTypeCrypt

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeCrypt: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeCrypt: String ``` |

Modified kODAuthenticationTypeDIGEST_MD5

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeDIGEST_MD5: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeDIGEST_MD5: String ``` |

Modified kODAuthenticationTypeDeleteUser

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeDeleteUser: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeDeleteUser: String ``` |

Modified kODAuthenticationTypeGetEffectivePolicy

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeGetEffectivePolicy: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeGetEffectivePolicy: String ``` |

Modified kODAuthenticationTypeGetGlobalPolicy

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeGetGlobalPolicy: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeGetGlobalPolicy: String ``` |

Modified kODAuthenticationTypeGetKerberosPrincipal

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeGetKerberosPrincipal: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeGetKerberosPrincipal: String ``` |

Modified kODAuthenticationTypeGetPolicy

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeGetPolicy: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeGetPolicy: String ``` |

Modified kODAuthenticationTypeGetUserData

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeGetUserData: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeGetUserData: String ``` |

Modified kODAuthenticationTypeGetUserName

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeGetUserName: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeGetUserName: String ``` |

Modified kODAuthenticationTypeKerberosTickets

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeKerberosTickets: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeKerberosTickets: String ``` |

Modified kODAuthenticationTypeMPPEMasterKeys

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeMPPEMasterKeys: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeMPPEMasterKeys: String ``` |

Modified kODAuthenticationTypeMSCHAP2

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeMSCHAP2: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeMSCHAP2: String ``` |

Modified kODAuthenticationTypeNTLMv2

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeNTLMv2: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeNTLMv2: String ``` |

Modified kODAuthenticationTypeNTLMv2WithSessionKey

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeNTLMv2WithSessionKey: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeNTLMv2WithSessionKey: String ``` |

Modified kODAuthenticationTypeNewUser

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeNewUser: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeNewUser: String ``` |

Modified kODAuthenticationTypeNewUserWithPolicy

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeNewUserWithPolicy: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeNewUserWithPolicy: String ``` |

Modified kODAuthenticationTypeNodeNativeClearTextOK

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeNodeNativeClearTextOK: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeNodeNativeClearTextOK: String ``` |

Modified kODAuthenticationTypeNodeNativeNoClearText

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeNodeNativeNoClearText: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeNodeNativeNoClearText: String ``` |

Modified kODAuthenticationTypeReadSecureHash

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeReadSecureHash: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeReadSecureHash: String ``` |

Modified kODAuthenticationTypeSMBNTv2UserSessionKey

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeSMBNTv2UserSessionKey: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeSMBNTv2UserSessionKey: String ``` |

Modified kODAuthenticationTypeSMBWorkstationCredentialSessionKey

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeSMBWorkstationCredentialSessionKey: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeSMBWorkstationCredentialSessionKey: String ``` |

Modified kODAuthenticationTypeSMB_LM_Key

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeSMB_LM_Key: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeSMB_LM_Key: String ``` |

Modified kODAuthenticationTypeSMB_NT_Key

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeSMB_NT_Key: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeSMB_NT_Key: String ``` |

Modified kODAuthenticationTypeSMB_NT_UserSessionKey

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeSMB_NT_UserSessionKey: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeSMB_NT_UserSessionKey: String ``` |

Modified kODAuthenticationTypeSMB_NT_WithUserSessionKey

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeSMB_NT_WithUserSessionKey: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeSMB_NT_WithUserSessionKey: String ``` |

Modified kODAuthenticationTypeSetCertificateHashAsCurrent

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kODAuthenticationTypeSetCertificateHashAsCurrent: ODAuthenticationType! ``` | OS X 10.10 |
| To | ``` let kODAuthenticationTypeSetCertificateHashAsCurrent: String ``` | OS X 10.7 |

Modified kODAuthenticationTypeSetGlobalPolicy

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeSetGlobalPolicy: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeSetGlobalPolicy: String ``` |

Modified kODAuthenticationTypeSetLMHash

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeSetLMHash: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeSetLMHash: String ``` |

Modified kODAuthenticationTypeSetNTHash

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeSetNTHash: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeSetNTHash: String ``` |

Modified kODAuthenticationTypeSetPassword

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeSetPassword: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeSetPassword: String ``` |

Modified kODAuthenticationTypeSetPasswordAsCurrent

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeSetPasswordAsCurrent: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeSetPasswordAsCurrent: String ``` |

Modified kODAuthenticationTypeSetPolicy

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeSetPolicy: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeSetPolicy: String ``` |

Modified kODAuthenticationTypeSetPolicyAsCurrent

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeSetPolicyAsCurrent: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeSetPolicyAsCurrent: String ``` |

Modified kODAuthenticationTypeSetUserData

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeSetUserData: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeSetUserData: String ``` |

Modified kODAuthenticationTypeSetUserName

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeSetUserName: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeSetUserName: String ``` |

Modified kODAuthenticationTypeSetWorkstationPassword

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeSetWorkstationPassword: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeSetWorkstationPassword: String ``` |

Modified kODAuthenticationTypeWithAuthorizationRef

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeWithAuthorizationRef: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeWithAuthorizationRef: String ``` |

Modified kODAuthenticationTypeWriteSecureHash

|  | Declaration |
| --- | --- |
| From | ``` let kODAuthenticationTypeWriteSecureHash: ODAuthenticationType! ``` |
| To | ``` let kODAuthenticationTypeWriteSecureHash: String ``` |

Modified kODErrorDomainFramework

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kODMatchInsensitiveBeginsWith

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.6 | OS X 10.10 |

Modified kODMatchInsensitiveContains

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.6 | OS X 10.10 |

Modified kODMatchInsensitiveEndsWith

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.6 | OS X 10.10 |

Modified kODMatchInsensitiveEqualTo

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.6 | OS X 10.10 |

Modified kODModuleConfigOptionConnectionIdleDisconnect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODModuleConfigOptionConnectionSetupTimeout

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODModuleConfigOptionManInTheMiddle

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODModuleConfigOptionPacketEncryption

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODModuleConfigOptionPacketSigning

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODModuleConfigOptionQueryTimeout

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODNodeOptionsQuerySkippedSubnode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kODPolicyAttributeCreationTime

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeCreationTime: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeCreationTime: String ``` |

Modified kODPolicyAttributeCurrentDate

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeCurrentDate: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeCurrentDate: String ``` |

Modified kODPolicyAttributeCurrentDayOfWeek

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeCurrentDayOfWeek: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeCurrentDayOfWeek: String ``` |

Modified kODPolicyAttributeCurrentTime

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeCurrentTime: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeCurrentTime: String ``` |

Modified kODPolicyAttributeCurrentTimeOfDay

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeCurrentTimeOfDay: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeCurrentTimeOfDay: String ``` |

Modified kODPolicyAttributeDaysUntilExpiration

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeDaysUntilExpiration: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeDaysUntilExpiration: String ``` |

Modified kODPolicyAttributeEnableAtTimeOfDay

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeEnableAtTimeOfDay: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeEnableAtTimeOfDay: String ``` |

Modified kODPolicyAttributeEnableOnDate

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeEnableOnDate: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeEnableOnDate: String ``` |

Modified kODPolicyAttributeEnableOnDayOfWeek

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeEnableOnDayOfWeek: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeEnableOnDayOfWeek: String ``` |

Modified kODPolicyAttributeExpiresAtTimeOfDay

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeExpiresAtTimeOfDay: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeExpiresAtTimeOfDay: String ``` |

Modified kODPolicyAttributeExpiresEveryNDays

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeExpiresEveryNDays: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeExpiresEveryNDays: String ``` |

Modified kODPolicyAttributeExpiresOnDate

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeExpiresOnDate: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeExpiresOnDate: String ``` |

Modified kODPolicyAttributeExpiresOnDayOfWeek

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeExpiresOnDayOfWeek: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeExpiresOnDayOfWeek: String ``` |

Modified kODPolicyAttributeFailedAuthentications

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeFailedAuthentications: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeFailedAuthentications: String ``` |

Modified kODPolicyAttributeLastAuthenticationTime

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeLastAuthenticationTime: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeLastAuthenticationTime: String ``` |

Modified kODPolicyAttributeLastFailedAuthenticationTime

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeLastFailedAuthenticationTime: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeLastFailedAuthenticationTime: String ``` |

Modified kODPolicyAttributeLastPasswordChangeTime

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeLastPasswordChangeTime: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeLastPasswordChangeTime: String ``` |

Modified kODPolicyAttributeMaximumFailedAuthentications

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeMaximumFailedAuthentications: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeMaximumFailedAuthentications: String ``` |

Modified kODPolicyAttributeNewPasswordRequiredTime

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeNewPasswordRequiredTime: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeNewPasswordRequiredTime: String ``` |

Modified kODPolicyAttributePassword

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributePassword: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributePassword: String ``` |

Modified kODPolicyAttributePasswordHashes

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributePasswordHashes: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributePasswordHashes: String ``` |

Modified kODPolicyAttributePasswordHistory

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributePasswordHistory: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributePasswordHistory: String ``` |

Modified kODPolicyAttributePasswordHistoryDepth

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributePasswordHistoryDepth: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributePasswordHistoryDepth: String ``` |

Modified kODPolicyAttributeRecordName

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeRecordName: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeRecordName: String ``` |

Modified kODPolicyAttributeRecordType

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyAttributeRecordType: ODPolicyAttributeType! ``` |
| To | ``` let kODPolicyAttributeRecordType: String ``` |

Modified kODPolicyCategoryAuthentication

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyCategoryAuthentication: ODPolicyCategoryType! ``` |
| To | ``` let kODPolicyCategoryAuthentication: String ``` |

Modified kODPolicyCategoryPasswordChange

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyCategoryPasswordChange: ODPolicyCategoryType! ``` |
| To | ``` let kODPolicyCategoryPasswordChange: String ``` |

Modified kODPolicyCategoryPasswordContent

|  | Declaration |
| --- | --- |
| From | ``` var kODPolicyCategoryPasswordContent: ODPolicyCategoryType! ``` |
| To | ``` let kODPolicyCategoryPasswordContent: String ``` |

Modified kODPolicyKeyContent

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyKeyContent: ODPolicyKeyType! ``` |
| To | ``` let kODPolicyKeyContent: String ``` |

Modified kODPolicyKeyIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyKeyIdentifier: ODPolicyKeyType! ``` |
| To | ``` let kODPolicyKeyIdentifier: String ``` |

Modified kODPolicyKeyParameters

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyKeyParameters: ODPolicyKeyType! ``` |
| To | ``` let kODPolicyKeyParameters: String ``` |

Modified kODPolicyTypeAccountExpiresOnDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODPolicyTypeAccountMaximumFailedLogins

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODPolicyTypeAccountMaximumMinutesOfNonUse

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODPolicyTypeAccountMaximumMinutesUntilDisabled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODPolicyTypeAccountMinutesUntilFailedLoginReset

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODPolicyTypePasswordCannotBeAccountName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODPolicyTypePasswordChangeRequired

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODPolicyTypePasswordHistory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODPolicyTypePasswordMaximumAgeInMinutes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODPolicyTypePasswordMaximumNumberOfCharacters

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODPolicyTypePasswordMinimumNumberOfCharacters

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODPolicyTypePasswordRequiresAlpha

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODPolicyTypePasswordRequiresMixedCase

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODPolicyTypePasswordRequiresNumeric

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODPolicyTypePasswordRequiresSymbol

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODPolicyTypePasswordSelfModification

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kODRecordTypeAFPServer

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeAFPServer: ODRecordType! ``` |
| To | ``` let kODRecordTypeAFPServer: String ``` |

Modified kODRecordTypeAliases

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeAliases: ODRecordType! ``` |
| To | ``` let kODRecordTypeAliases: String ``` |

Modified kODRecordTypeAttributeTypes

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeAttributeTypes: ODRecordType! ``` |
| To | ``` let kODRecordTypeAttributeTypes: String ``` |

Modified kODRecordTypeAugments

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeAugments: ODRecordType! ``` |
| To | ``` let kODRecordTypeAugments: String ``` |

Modified kODRecordTypeAutoServerSetup

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeAutoServerSetup: ODRecordType! ``` |
| To | ``` let kODRecordTypeAutoServerSetup: String ``` |

Modified kODRecordTypeAutomount

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeAutomount: ODRecordType! ``` |
| To | ``` let kODRecordTypeAutomount: String ``` |

Modified kODRecordTypeAutomountMap

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeAutomountMap: ODRecordType! ``` |
| To | ``` let kODRecordTypeAutomountMap: String ``` |

Modified kODRecordTypeBootp

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeBootp: ODRecordType! ``` |
| To | ``` let kODRecordTypeBootp: String ``` |

Modified kODRecordTypeCertificateAuthorities

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeCertificateAuthorities: ODRecordType! ``` |
| To | ``` let kODRecordTypeCertificateAuthorities: String ``` |

Modified kODRecordTypeComputerGroups

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeComputerGroups: ODRecordType! ``` |
| To | ``` let kODRecordTypeComputerGroups: String ``` |

Modified kODRecordTypeComputerLists

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeComputerLists: ODRecordType! ``` |
| To | ``` let kODRecordTypeComputerLists: String ``` |

Modified kODRecordTypeComputers

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeComputers: ODRecordType! ``` |
| To | ``` let kODRecordTypeComputers: String ``` |

Modified kODRecordTypeConfiguration

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeConfiguration: ODRecordType! ``` |
| To | ``` let kODRecordTypeConfiguration: String ``` |

Modified kODRecordTypeEthernets

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeEthernets: ODRecordType! ``` |
| To | ``` let kODRecordTypeEthernets: String ``` |

Modified kODRecordTypeFTPServer

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeFTPServer: ODRecordType! ``` |
| To | ``` let kODRecordTypeFTPServer: String ``` |

Modified kODRecordTypeFileMakerServers

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeFileMakerServers: ODRecordType! ``` |
| To | ``` let kODRecordTypeFileMakerServers: String ``` |

Modified kODRecordTypeGroups

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeGroups: ODRecordType! ``` |
| To | ``` let kODRecordTypeGroups: String ``` |

Modified kODRecordTypeHostServices

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeHostServices: ODRecordType! ``` |
| To | ``` let kODRecordTypeHostServices: String ``` |

Modified kODRecordTypeHosts

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeHosts: ODRecordType! ``` |
| To | ``` let kODRecordTypeHosts: String ``` |

Modified kODRecordTypeLDAPServer

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeLDAPServer: ODRecordType! ``` |
| To | ``` let kODRecordTypeLDAPServer: String ``` |

Modified kODRecordTypeLocations

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeLocations: ODRecordType! ``` |
| To | ``` let kODRecordTypeLocations: String ``` |

Modified kODRecordTypeMounts

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeMounts: ODRecordType! ``` |
| To | ``` let kODRecordTypeMounts: String ``` |

Modified kODRecordTypeNFS

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeNFS: ODRecordType! ``` |
| To | ``` let kODRecordTypeNFS: String ``` |

Modified kODRecordTypeNetDomains

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeNetDomains: ODRecordType! ``` |
| To | ``` let kODRecordTypeNetDomains: String ``` |

Modified kODRecordTypeNetGroups

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeNetGroups: ODRecordType! ``` |
| To | ``` let kODRecordTypeNetGroups: String ``` |

Modified kODRecordTypeNetworks

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeNetworks: ODRecordType! ``` |
| To | ``` let kODRecordTypeNetworks: String ``` |

Modified kODRecordTypePeople

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypePeople: ODRecordType! ``` |
| To | ``` let kODRecordTypePeople: String ``` |

Modified kODRecordTypePresetComputerGroups

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypePresetComputerGroups: ODRecordType! ``` |
| To | ``` let kODRecordTypePresetComputerGroups: String ``` |

Modified kODRecordTypePresetComputerLists

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypePresetComputerLists: ODRecordType! ``` |
| To | ``` let kODRecordTypePresetComputerLists: String ``` |

Modified kODRecordTypePresetComputers

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypePresetComputers: ODRecordType! ``` |
| To | ``` let kODRecordTypePresetComputers: String ``` |

Modified kODRecordTypePresetGroups

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypePresetGroups: ODRecordType! ``` |
| To | ``` let kODRecordTypePresetGroups: String ``` |

Modified kODRecordTypePresetUsers

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypePresetUsers: ODRecordType! ``` |
| To | ``` let kODRecordTypePresetUsers: String ``` |

Modified kODRecordTypePrintService

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypePrintService: ODRecordType! ``` |
| To | ``` let kODRecordTypePrintService: String ``` |

Modified kODRecordTypePrintServiceUser

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypePrintServiceUser: ODRecordType! ``` |
| To | ``` let kODRecordTypePrintServiceUser: String ``` |

Modified kODRecordTypePrinters

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypePrinters: ODRecordType! ``` |
| To | ``` let kODRecordTypePrinters: String ``` |

Modified kODRecordTypeProtocols

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeProtocols: ODRecordType! ``` |
| To | ``` let kODRecordTypeProtocols: String ``` |

Modified kODRecordTypeQTSServer

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeQTSServer: ODRecordType! ``` |
| To | ``` let kODRecordTypeQTSServer: String ``` |

Modified kODRecordTypeQueryInformation

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeQueryInformation: ODRecordType! ``` |
| To | ``` let kODRecordTypeQueryInformation: String ``` |

Modified kODRecordTypeRPC

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeRPC: ODRecordType! ``` |
| To | ``` let kODRecordTypeRPC: String ``` |

Modified kODRecordTypeRecordTypes

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeRecordTypes: ODRecordType! ``` |
| To | ``` let kODRecordTypeRecordTypes: String ``` |

Modified kODRecordTypeResources

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeResources: ODRecordType! ``` |
| To | ``` let kODRecordTypeResources: String ``` |

Modified kODRecordTypeSMBServer

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeSMBServer: ODRecordType! ``` |
| To | ``` let kODRecordTypeSMBServer: String ``` |

Modified kODRecordTypeServer

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeServer: ODRecordType! ``` |
| To | ``` let kODRecordTypeServer: String ``` |

Modified kODRecordTypeServices

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeServices: ODRecordType! ``` |
| To | ``` let kODRecordTypeServices: String ``` |

Modified kODRecordTypeSharePoints

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeSharePoints: ODRecordType! ``` |
| To | ``` let kODRecordTypeSharePoints: String ``` |

Modified kODRecordTypeUsers

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeUsers: ODRecordType! ``` |
| To | ``` let kODRecordTypeUsers: String ``` |

Modified kODRecordTypeWebServer

|  | Declaration |
| --- | --- |
| From | ``` let kODRecordTypeWebServer: ODRecordType! ``` |
| To | ``` let kODRecordTypeWebServer: String ``` |

Modified kODSessionDefault

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kODSessionProxyAddress

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kODSessionProxyPassword

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kODSessionProxyPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kODSessionProxyUsername

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

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
