---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/OpenDirectory.html
archived_at: '2026-07-15T07:34:47.003204Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# OpenDirectory Changes

## OpenDirectory

CFODNode.hAdded [ODNodeAddAccountPolicy()](https://developer.apple.com/documentation/opendirectory/1427169-odnodeaddaccountpolicy)Added [ODNodeCopyAccountPolicies()](https://developer.apple.com/documentation/opendirectory/1427963-odnodecopyaccountpolicies)Added [ODNodePasswordContentCheck()](https://developer.apple.com/documentation/opendirectory/1426938-odnodepasswordcontentcheck)Added [ODNodeRemoveAccountPolicy()](https://developer.apple.com/documentation/opendirectory/1427805-odnoderemoveaccountpolicy)Added [ODNodeSetAccountPolicies()](https://developer.apple.com/documentation/opendirectory/1427971-odnodesetaccountpolicies)Modified [ODNodeCopyPolicies()](https://developer.apple.com/documentation/opendirectory/1426916-odnodecopypolicies)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [ODNodeCopySupportedPolicies()](https://developer.apple.com/documentation/opendirectory/1427601-odnodecopysupportedpolicies)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [ODNodeRemovePolicy()](https://developer.apple.com/documentation/opendirectory/1427219-odnoderemovepolicy)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [ODNodeSetPolicies()](https://developer.apple.com/documentation/opendirectory/1427235-odnodesetpolicies)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [ODNodeSetPolicy()](https://developer.apple.com/documentation/opendirectory/1427861-odnodesetpolicy)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

CFODRecord.hAdded [ODRecordAddAccountPolicy()](https://developer.apple.com/documentation/opendirectory/1427181-odrecordaddaccountpolicy)Added [ODRecordAuthenticationAllowed()](https://developer.apple.com/documentation/opendirectory/1427977-odrecordauthenticationallowed)Added [ODRecordCopyAccountPolicies()](https://developer.apple.com/documentation/opendirectory/1427023-odrecordcopyaccountpolicies)Added [ODRecordPasswordChangeAllowed()](https://developer.apple.com/documentation/opendirectory/1427135-odrecordpasswordchangeallowed)Added [ODRecordRemoveAccountPolicy()](https://developer.apple.com/documentation/opendirectory/1427675-odrecordremoveaccountpolicy)Added [ODRecordSecondsUntilAuthenticationsExpire()](https://developer.apple.com/documentation/opendirectory/1427380-odrecordsecondsuntilauthenticati)Added [ODRecordSecondsUntilPasswordExpires()](https://developer.apple.com/documentation/opendirectory/1427195-odrecordsecondsuntilpasswordexpi)Added [ODRecordSetAccountPolicies()](https://developer.apple.com/documentation/opendirectory/1427703-odrecordsetaccountpolicies)Added [ODRecordWillAuthenticationsExpire()](https://developer.apple.com/documentation/opendirectory/1427171-odrecordwillauthenticationsexpir)Added [ODRecordWillPasswordExpire()](https://developer.apple.com/documentation/opendirectory/1427185-odrecordwillpasswordexpire)Modified [ODRecordCopyEffectivePolicies()](https://developer.apple.com/documentation/opendirectory/1427362-odrecordcopyeffectivepolicies)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [ODRecordCopyPolicies()](https://developer.apple.com/documentation/opendirectory/1427298-odrecordcopypolicies)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [ODRecordCopySupportedPolicies()](https://developer.apple.com/documentation/opendirectory/1427055-odrecordcopysupportedpolicies)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [ODRecordRemovePolicy()](https://developer.apple.com/documentation/opendirectory/1427063-odrecordremovepolicy)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [ODRecordSetPolicies()](https://developer.apple.com/documentation/opendirectory/1427387-odrecordsetpolicies)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [ODRecordSetPolicy()](https://developer.apple.com/documentation/opendirectory/1428137-odrecordsetpolicy)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

CFOpenDirectoryConstants.hAdded [ODPolicyAttributeType](https://developer.apple.com/documentation/opendirectory/odpolicyattributetype)Added [ODPolicyCategoryType](https://developer.apple.com/documentation/opendirectory/odpolicycategorytype)Added [ODPolicyKeyType](https://developer.apple.com/documentation/opendirectory/odpolicykeytype)Added [kODExpirationTimeExpired](https://developer.apple.com/documentation/opendirectory/1497721-anonymous/kodexpirationtimeexpired)Added [kODExpirationTimeNeverExpires](https://developer.apple.com/documentation/opendirectory/kodexpirationtimeneverexpires)Added [kODPolicyAttributeCreationTime](https://developer.apple.com/documentation/opendirectory/kodpolicyattributecreationtime)Added [kODPolicyAttributeCurrentDate](https://developer.apple.com/documentation/opendirectory/kodpolicyattributecurrentdate)Added [kODPolicyAttributeCurrentDayOfWeek](https://developer.apple.com/documentation/opendirectory/kodpolicyattributecurrentdayofweek)Added [kODPolicyAttributeCurrentTime](https://developer.apple.com/documentation/opendirectory/kodpolicyattributecurrenttime)Added [kODPolicyAttributeCurrentTimeOfDay](https://developer.apple.com/documentation/opendirectory/kodpolicyattributecurrenttimeofday)Added [kODPolicyAttributeDaysUntilExpiration](https://developer.apple.com/documentation/opendirectory/kodpolicyattributedaysuntilexpiration)Added [kODPolicyAttributeEnableAtTimeOfDay](https://developer.apple.com/documentation/opendirectory/kodpolicyattributeenableattimeofday)Added [kODPolicyAttributeEnableOnDate](https://developer.apple.com/documentation/opendirectory/kodpolicyattributeenableondate)Added [kODPolicyAttributeEnableOnDayOfWeek](https://developer.apple.com/documentation/opendirectory/kodpolicyattributeenableondayofweek)Added [kODPolicyAttributeExpiresAtTimeOfDay](https://developer.apple.com/documentation/opendirectory/kodpolicyattributeexpiresattimeofday)Added [kODPolicyAttributeExpiresEveryNDays](https://developer.apple.com/documentation/opendirectory/kodpolicyattributeexpireseveryndays)Added [kODPolicyAttributeExpiresOnDate](https://developer.apple.com/documentation/opendirectory/kodpolicyattributeexpiresondate)Added [kODPolicyAttributeExpiresOnDayOfWeek](https://developer.apple.com/documentation/opendirectory/kodpolicyattributeexpiresondayofweek)Added [kODPolicyAttributeFailedAuthentications](https://developer.apple.com/documentation/opendirectory/kodpolicyattributefailedauthentications)Added [kODPolicyAttributeLastAuthenticationTime](https://developer.apple.com/documentation/opendirectory/kodpolicyattributelastauthenticationtime)Added [kODPolicyAttributeLastFailedAuthenticationTime](https://developer.apple.com/documentation/opendirectory/kodpolicyattributelastfailedauthenticationtime)Added [kODPolicyAttributeLastPasswordChangeTime](https://developer.apple.com/documentation/opendirectory/kodpolicyattributelastpasswordchangetime)Added [kODPolicyAttributeMaximumFailedAuthentications](https://developer.apple.com/documentation/opendirectory/kodpolicyattributemaximumfailedauthentications)Added [kODPolicyAttributeNewPasswordRequiredTime](https://developer.apple.com/documentation/opendirectory/kodpolicyattributenewpasswordrequiredtime)Added [kODPolicyAttributePassword](https://developer.apple.com/documentation/opendirectory/kodpolicyattributepassword)Added [kODPolicyAttributePasswordHashes](https://developer.apple.com/documentation/opendirectory/kodpolicyattributepasswordhashes)Added [kODPolicyAttributePasswordHistory](https://developer.apple.com/documentation/opendirectory/kodpolicyattributepasswordhistory)Added [kODPolicyAttributePasswordHistoryDepth](https://developer.apple.com/documentation/opendirectory/kodpolicyattributepasswordhistorydepth)Added [kODPolicyAttributeRecordName](https://developer.apple.com/documentation/opendirectory/kodpolicyattributerecordname)Added [kODPolicyAttributeRecordType](https://developer.apple.com/documentation/opendirectory/kodpolicyattributerecordtype)Added [kODPolicyCategoryAuthentication](https://developer.apple.com/documentation/opendirectory/kodpolicycategoryauthentication)Added [kODPolicyCategoryPasswordChange](https://developer.apple.com/documentation/opendirectory/kodpolicycategorypasswordchange)Added [kODPolicyCategoryPasswordContent](https://developer.apple.com/documentation/opendirectory/kodpolicycategorypasswordcontent)Added [kODPolicyKeyContent](https://developer.apple.com/documentation/opendirectory/kodpolicykeycontent)Added [kODPolicyKeyIdentifier](https://developer.apple.com/documentation/opendirectory/kodpolicykeyidentifier)Added [kODPolicyKeyParameters](https://developer.apple.com/documentation/opendirectory/kodpolicykeyparameters)Modified [kODMatchInsensitiveBeginsWith](https://developer.apple.com/documentation/opendirectory/kodmatchinsensitivebeginswith)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [kODMatchInsensitiveContains](https://developer.apple.com/documentation/opendirectory/kodmatchinsensitivecontains)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [kODMatchInsensitiveEndsWith](https://developer.apple.com/documentation/opendirectory/kodmatchinsensitiveendswith)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [kODMatchInsensitiveEqualTo](https://developer.apple.com/documentation/opendirectory/kodmatchinsensitiveequalto)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

ODAttributeMap.hModified [+[ODAttributeMap attributeMapWithStaticValue:]](https://developer.apple.com/documentation/opendirectory/odattributemap/1427869-attributemapwithstaticvalue)

|  | Declaration |
| --- | --- |
| From | ``` + (id)attributeMapWithStaticValue:(NSString *)staticValue ``` |
| To | ``` + (instancetype)attributeMapWithStaticValue:(NSString *)staticValue ``` |

Modified [+[ODAttributeMap attributeMapWithValue:]](https://developer.apple.com/documentation/opendirectory/odattributemap/1428209-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)attributeMapWithValue:(NSString *)value ``` |
| To | ``` + (instancetype)attributeMapWithValue:(NSString *)value ``` |

ODConfiguration.hModified [+[ODConfiguration configuration]](https://developer.apple.com/documentation/opendirectory/odconfiguration/1579650-configuration)

|  | Declaration |
| --- | --- |
| From | ``` + (id)configuration ``` |
| To | ``` + (instancetype)configuration ``` |

ODMappings.hModified [+[ODMappings mappings]](https://developer.apple.com/documentation/opendirectory/odmappings/1528311-mappings)

|  | Declaration |
| --- | --- |
| From | ``` + (id)mappings ``` |
| To | ``` + (instancetype)mappings ``` |

ODModuleEntry.hModified [+[ODModuleEntry moduleEntryWithName:xpcServiceName:]](https://developer.apple.com/documentation/opendirectory/odmoduleentry/1426940-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)moduleEntryWithName:(NSString *)name xpcServiceName:(NSString *)xpcServiceName ``` |
| To | ``` + (instancetype)moduleEntryWithName:(NSString *)name xpcServiceName:(NSString *)xpcServiceName ``` |

ODNode.hRemoved -[ODNode configuration]Added [-[ODNode accountPoliciesAndReturnError:]](https://developer.apple.com/documentation/opendirectory/odnode/1428081-accountpolicies)Added [-[ODNode addAccountPolicy:toCategory:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1427951-addaccountpolicy)Added [ODNode.configuration](https://developer.apple.com/documentation/opendirectory/odnode/1428039-configuration)Added [-[ODNode passwordContentCheck:forRecordName:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1427933-passwordcontentcheck)Added [-[ODNode removeAccountPolicy:fromCategory:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1427267-removeaccountpolicy)Added [-[ODNode setAccountPolicies:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1426999-setaccountpolicies)Modified [-[ODNode initWithSession:name:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1428278-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithSession:(ODSession *)inSession name:(NSString *)inName error:(NSError **)outError ``` |
| To | ``` - (instancetype)initWithSession:(ODSession *)inSession name:(NSString *)inName error:(NSError **)outError ``` |

Modified [-[ODNode initWithSession:type:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1427701-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithSession:(ODSession *)inSession type:(ODNodeType)inType error:(NSError **)outError ``` |
| To | ``` - (instancetype)initWithSession:(ODSession *)inSession type:(ODNodeType)inType error:(NSError **)outError ``` |

Modified [+[ODNode nodeWithSession:name:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1569409-nodewithsession)

|  | Declaration |
| --- | --- |
| From | ``` + (id)nodeWithSession:(ODSession *)inSession name:(NSString *)inName error:(NSError **)outError ``` |
| To | ``` + (instancetype)nodeWithSession:(ODSession *)inSession name:(NSString *)inName error:(NSError **)outError ``` |

Modified [+[ODNode nodeWithSession:type:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1569410-nodewithsession)

|  | Declaration |
| --- | --- |
| From | ``` + (id)nodeWithSession:(ODSession *)inSession type:(ODNodeType)inType error:(NSError **)outError ``` |
| To | ``` + (instancetype)nodeWithSession:(ODSession *)inSession type:(ODNodeType)inType error:(NSError **)outError ``` |

Modified [-[ODNode policiesAndReturnError:]](https://developer.apple.com/documentation/opendirectory/odnode/1428217-policies)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[ODNode removePolicy:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1427245-removepolicy)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[ODNode setPolicies:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1426946-setpolicies)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[ODNode setPolicy:value:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1428225-setpolicy)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[ODNode supportedPoliciesAndReturnError:]](https://developer.apple.com/documentation/opendirectory/odnode/1428033-supportedpolicies)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

ODQuery.hModified [-[ODQuery initWithNode:forRecordTypes:attribute:matchType:queryValues:returnAttributes:maximumResults:error:]](https://developer.apple.com/documentation/opendirectory/odquery/1391711-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithNode:(ODNode *)inNode forRecordTypes:(id)inRecordTypeOrList attribute:(ODAttributeType)inAttribute matchType:(ODMatchType)inMatchType queryValues:(id)inQueryValueOrList returnAttributes:(id)inReturnAttributeOrList maximumResults:(NSInteger)inMaximumResults error:(NSError **)outError ``` |
| To | ``` - (instancetype)initWithNode:(ODNode *)inNode forRecordTypes:(id)inRecordTypeOrList attribute:(ODAttributeType)inAttribute matchType:(ODMatchType)inMatchType queryValues:(id)inQueryValueOrList returnAttributes:(id)inReturnAttributeOrList maximumResults:(NSInteger)inMaximumResults error:(NSError **)outError ``` |

ODRecord.hAdded [-[ODRecord accountPoliciesAndReturnError:]](https://developer.apple.com/documentation/opendirectory/odrecord/1428124-accountpolicies)Added [-[ODRecord addAccountPolicy:toCategory:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427406-addaccountpolicy)Added [-[ODRecord authenticationAllowedAndReturnError:]](https://developer.apple.com/documentation/opendirectory/odrecord/1428106-authenticationallowedandreturner)Added [-[ODRecord passwordChangeAllowed:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427623-passwordchangeallowed)Added [-[ODRecord removeAccountPolicy:fromCategory:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427577-removeaccountpolicy)Added [ODRecord.secondsUntilAuthenticationsExpire](https://developer.apple.com/documentation/opendirectory/odrecord/1428115-secondsuntilauthenticationsexpir)Added [ODRecord.secondsUntilPasswordExpires](https://developer.apple.com/documentation/opendirectory/odrecord/1428282-secondsuntilpasswordexpires)Added [-[ODRecord setAccountPolicies:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427241-setaccountpolicies)Added [-[ODRecord willAuthenticationsExpire:]](https://developer.apple.com/documentation/opendirectory/odrecord/1428178-willauthenticationsexpire)Added [-[ODRecord willPasswordExpire:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427767-willpasswordexpire)Modified [-[ODRecord effectivePoliciesAndReturnError:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427296-effectivepolicies)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[ODRecord policiesAndReturnError:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427995-policies)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[ODRecord removePolicy:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427589-removepolicy)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[ODRecord setPolicies:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427266-setpolicies)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[ODRecord setPolicy:value:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427191-setpolicy)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[ODRecord supportedPoliciesAndReturnError:]](https://developer.apple.com/documentation/opendirectory/odrecord/1428172-supportedpolicies)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

ODRecordMap.hModified [+[ODRecordMap recordMap]](https://developer.apple.com/documentation/opendirectory/odrecordmap/1547303-recordmap)

|  | Declaration |
| --- | --- |
| From | ``` + (id)recordMap ``` |
| To | ``` + (instancetype)recordMap ``` |

ODSession.hRemoved -[ODSession configurationTemplateNames]Removed -[ODSession mappingTemplateNames]Added [ODSession.configurationTemplateNames](https://developer.apple.com/documentation/opendirectory/odsession/1427783-configurationtemplatenames)Added [ODSession.mappingTemplateNames](https://developer.apple.com/documentation/opendirectory/odsession/1427663-mappingtemplatenames)Modified [+[ODSession defaultSession]](https://developer.apple.com/documentation/opendirectory/odsession/1428153-default)

|  | Declaration |
| --- | --- |
| From | ``` + (id)defaultSession ``` |
| To | ``` + (ODSession *)defaultSession ``` |

Modified [-[ODSession initWithOptions:error:]](https://developer.apple.com/documentation/opendirectory/odsession/1427223-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithOptions:(NSDictionary *)inOptions error:(NSError **)outError ``` |
| To | ``` - (instancetype)initWithOptions:(NSDictionary *)inOptions error:(NSError **)outError ``` |

Modified [+[ODSession sessionWithOptions:error:]](https://developer.apple.com/documentation/opendirectory/odsession/1563458-sessionwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` + (id)sessionWithOptions:(NSDictionary *)inOptions error:(NSError **)outError ``` |
| To | ``` + (instancetype)sessionWithOptions:(NSDictionary *)inOptions error:(NSError **)outError ``` |

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
