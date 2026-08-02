---
title: iSync SyncML Guide
apple_id: TP40004561
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-06-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/iSyncSyncMLGuide/iSyncSyncMLGuide.pdf
archived_at: '2026-07-27T06:32:34.000980Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)



# iSync SyncML Guide

[打开 Apple 原始 PDF](attachments/original.pdf)

## 第 1 页

iSync SyncML Guide
2006-07-14

## 第 2 页

AppleComputerrInct
©xvv6AppleComputerrInct
Allrightsreservedt
Nopartofthispublicationmaybe
reproducedrstoredinaretrievalsystemror
transmittedrinanyformorbyanymeansr
mechanicalrelectronicrphotocopyingr
recordingrorotherwiserwithoutprior
writtenpermissionofAppleComputerrInctr
withthefollowingexceptions:Anyperson
isherebyauthorizedtostoredocumentation
onasinglecomputerforpersonaluseonly
andtoprintcopiesofdocumentationfor
personaluseprovidedthatthe
documentationcontainsApple’scopyright
noticet
TheApplelogoisatrademarkofApple
ComputerrInct
Useofthe“keyboard”Applelogo
mOptionsShiftsKnforcommercialpurposes
withoutthepriorwrittenconsentofApple
mayconstitutetrademarkinfringementand
unfaircompetitioninviolationoffederal
andstatelawst
Nolicensesrexpressorimpliedraregranted
withrespecttoanyofthetechnology
describedinthisdocumenttAppleretains
allintellectualpropertyrightsassociated
withthetechnologydescribedinthis
documenttThisdocumentisintendedto
assistapplicationdeveloperstodevelop
applicationsonlyforAppleslabeledor
Appleslicensedcomputerst
Everyefforthasbeenmadetoensurethat
theinformationinthisdocumentis
accuratetAppleisnotresponsiblefor
typographicalerrorst
AppleComputerrInct
wInfiniteLoop
CupertinorCA9©vwz
zv8s996swvwv
ApplertheApplelogoriCalrMacrMacOSr
andMacintosharetrademarksofApple
ComputerrInctrregisteredintheUnited
Statesandothercountriest
FinderisatrademarkofAppleComputerr
Inct
JavaandallJavasbasedtrademarksare
trademarksorregisteredtrademarksofSun
MicrosystemsrInctintheUtStandother
countriest
SimultaneouslypublishedintheUnited
StatesandCanadat
EventhoughApplehasreviewedthisdocuments
APPLEMAKESNOWARRANTYOR
REPRESENTATIONsEITHEREXPRESSOR
IMPLIEDsWITHRESPECTTOTHIS
DOCUMENTsITSQUALITYsACCURACYs
MERCHANTABILITYsORFITNESSFORA
PARTICULARPURPOSEuASARESULTsTHIS
DOCUMENTISPROVIDED“ASISs”AND
YOUsTHEREADERsAREASSUMINGTHE
ENTIRERISKASTOITSQUALITYAND
ACCURACYu
INNOEVENTWILLAPPLEBELIABLEFOR
DIRECTsINDIRECTsSPECIALsINCIDENTALs
ORCONSEQUENTIALDAMAGES
RESULTINGFROMANYDEFECTOR
INACCURACYINTHISDOCUMENTsevenif
advisedofthepossibilityofsuchdamagesu
THEWARRANTYANDREMEDIESSET
FORTHABOVEAREEXCLUSIVEANDIN
LIEUOFALLOTHERSsORALORWRITTENs
EXPRESSORIMPLIEDuNoAppledealersagents
oremployeeisauthorizedtomakeany
modificationsextensionsoradditiontothis
warrantyu
Somestatesdonotallowtheexclusionor
limitationofimpliedwarrantiesorliabilityfor
incidentalorconsequentialdamagesssothe
abovelimitationorexclusionmaynotapplyto
youuThiswarrantygivesyouspecificlegal
rightssandyoumayalsohaveotherrightswhich
varyfromstatetostateu

## 第 3 页

Table of Contents
Introduction 3
References 4
Conventions 6
SyncML Support Overview 7
Encoding 7
Version 7
Transport 7
Authentication 7
Large Objects 7
Sync Types 7
Server Alert 9
SyncML 1.1.2 Server Alert Examples 9
Separate Databases for Events and Tasks 9
Common Database for Events and Tasks 10
SyncML 1.2 SAN example 11
Separate Databases for Events and Tasks 11
Common Database for Events and Tasks 12
A Device Database Reset 14
Last Anchor Is Not Present 14
Last Anchor Is '00000000T000000Z' 14
Last Anchor Is 0, and 'Next Anchor' Is 0 15
Last Anchor Is 0, and 'Next Anchor' Was > 0 During the Previous SyncML
Session with That Device 15
Busy Signaling 17
Example of a Session with a Busy Signaling Message 17
iSync SyncML Guide 1

## 第 4 页

Busy Signaling Not Supported 22
Only One Busy Signaling Message Is Supported 27
Databases 28
vCard 28
Supported Fields 28
Type Mapping 29
Delivery address (ADR) 29
Email (EMAIL) 29
Phone (TEL) 30
URL (URL) 30
vCal 30
Supported Fields 30
All Day Event 31
OMA Formatting 31
From Midnight to Midnight (the day after) 32
Using the CATEGORIES property 32
From Midnight to 23:59 33
Recurrences Rules 33
iSync SyncML Guide 2

## 第 5 页

1. Introduction
This document describes specific aspects of the Open Mobile Alliance (OMA) SyncML
implementation in iSync. Its goal is to serve as a guide for developers of SyncML clients and phone
plug-ins.
Note:
The Open Mobile Alliance (OMA) Data Synchronization Working Group is developing
specifications for data synchronization that includes SyncML technology. This book refers to
the data synchronization technology as SyncML.
iSync SyncML Guide 3

## 第 6 页

2. References
This section contains references to specifications of SyncML and other related technologies.
OMA SyncML Common Specifications V1.1.2
[SYNCREPRO-1.1.2] SyncML Representation Protocol, Version 1.1.2,
URL:http://www.openmobilealliance.org/release_program/SyncML_v112.html
[SYNCMETA-1.1.2] SyncML Meta Information, Version 1.1.2,
URL:http://www.openmobilealliance.org/release_program/SyncML_v112.html
[SYNCHTTP-1.1.2] SyncML HTTP Binding, Version 1.1.2,
URL:http://www.openmobilealliance.org/release_program/SyncML_v112.html
[SYNCOBEX-1.1.2] SyncML OBEX Binding, Version 1.1.2,
URL:http://www.openmobilealliance.org/release_program/SyncML_v112.html
[SYNCWSP-1.1.2] SyncML WSP Binding, Version 1.1.2,
URL:http://www.openmobilealliance.org/release_program/SyncML_v112.html
OMA SyncML Data Synchronization Specifications V1.1.2
[DSREPRO-1.1.2] SyncML Representation Protocol, Data Synchronization Usage, Version 1.1.2,
URL:http:www.openmobilealliance.org/release_program/ds_v112.html
[DSPRO-1.1.2] SyncML Data Sync Protocol, Version 1.1.2,
URL:http:www.openmobilealliance.org/release_program/ds_v112.html
[DSDEVINF-1.1.2] SyncML Device Information, Version 1.1.2,
URL:http:www.openmobilealliance.org/release_program/ds_v112.html
OMA SyncML Common Specifications V1.2
[SYNCREPRO-1.2] SyncML Representation Protocol, Version 1.2,
URL:http://www.openmobilealliance.org/release_program/SyncML_v12.html
[SYNCMETA-1.2] SyncML Meta Information, Version 1.2,
URL:http://www.openmobilealliance.org/release_program/SyncML_v12.html
[SYNCSAN-1.2] SyncML Server Alerted Notiﬁcation,
URL:http://www.openmobilealliance.org/release_program/SyncML_v12.html
[SYNCHTTP-1.2] SyncML HTTP Binding, Version 1.2,
URL:http://www.openmobilealliance.org/release_program/SyncML_v12.html
iSync SyncML Guide 4

## 第 7 页

OMA SyncML Common Specifications V1.2
[SYNCOBEX-1.2] SyncML OBEX Binding, Version 1.2,
URL:http://www.openmobilealliance.org/release_program/SyncML_v12.html
[SYNCWSP-1.2] SyncML WSP Binding, Version 1.2,
URL:http://www.openmobilealliance.org/release_program/SyncML_v12.html
OMA SyncML Data Synchronization Specifications V1.2
[DSREPRO-1.2] SyncML Representation Protocol, Data Synchronization Usage, Version 1.2,
URL:http://www.openmobilealliance.org/release_program/ds_v12.html
[DSPRO-1.2] SyncML Data Sync Protocol, Version 1.2,
URL:http://www.openmobilealliance.org/release_program/ds_v12.html
[DSDEVINF-1.2] SyncML Device Information, Version 1.2,
URL:http://www.openmobilealliance.org/release_program/ds_v12.html
[DSEMAIL-1.2] SyncML Email  Data Object Speciﬁcation,
URL:http://www.openmobilealliance.org/release_program/ds_v12.html
[DSFILE-1.2] SyncML File  Data Object Speciﬁcation,
URL:http://www.openmobilealliance.org/release_program/ds_v12.html
[DSFOLDER-1.2] SyncML Folder  Data Object Speciﬁcation,
URL:http://www.openmobilealliance.org/release_program/ds_v12.html
Other Specifications
[IMCVCAL-1.0] “vCalendar – The electronic calendaring and scheduling exchange
format – Version 1.0”,
URL:http://www.imc.org/pdi/vcal-10.doc
[IMCVCARD-2.1] “vCard - The electronic business card - Version 2.1”,
URL:http://www.imc.org/pdi/vcard-21.doc
[VOBJPROFILE-1.0] “vObject minimum interoperability profile V1.0”,
URL:http://www.openmobilealliance.org
[RFC2119] “Key words for use in RFCs to Indicate Requirement Levels”
S. Bradner,  March 1997,
URL:http://www.ietf.org/rfc/rfc2119.txt
iSync SyncML Guide 5

## 第 8 页

3. Conventions
The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD
NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as
described in [RFC2119].
iSync SyncML Guide 6

## 第 9 页

4. SyncML Support Overview
This section provides an overview of the SyncML features supported by iSync.
4.1. Encoding
iSync supports WBXML format, not XML.
4.2. Version
iSync supports SyncML 1.1.2 and SyncML 1.2.
The only SyncML 1.2 specific features currently supported are:
•The new Server Alert Notiﬁcation (SAN) format, with an empty Digest ﬁeld.
•The new DevInf format.
•Suspend / Resume feature. Note that for now the iSync implementation forces a slow sync when the client
tries to resume the sync session.
4.3. Transport
iSync supports only local sync (BT and USB) over OBEX.
4.4. Authentication
The SyncML authentication mechanism is NOT supported.
4.5. Large Objects
The SyncML client SHOULD support “Large Objects” as soon as the client supports contact picture
synchronization.
4.6. Sync Types
•A SyncML client MUST support “Sync Alert”.
•A client initiated sync is NOT supported by iSync.
•A SyncML client MUST NOT initiate a “Sync without Separate Initialization”.
iSync SyncML Guide 7

## 第 10 页

•A SyncML client SHOULD support Refresh Sync From Server Only for better performance. This mode is
described in section 12.5 of [DSPRO-1.1.2]. If a SyncML client does not support this sync type, then iSync will
do a Slow Reset: A Slow Sync is initiated, and a Delete command is sent on each device’s record.
iSync SyncML Guide 8

## 第 11 页

5. Server Alert
iSync provides its database names in the Server Alert package (Pkg#0). A SyncML client MUST
use those names in following messages.
•If SyncML 1.1.2 is used, a SyncML client MUST support a Server Alerted Sync, as deﬁned in section 13 of
[DSPRO-1.1.2].
•If SyncML 1.2 is used, a client MUST support Server Alert Notiﬁcation (SAN), as described in [SYNCSAN-1.2]
and section 12 of [DSPRO-1.2].
5.1. SyncML 1.1.2 Server Alert Examples
Here are some examples of SyncML 1.1.2 Server Alert packages that iSync sends. Depending on
the phone plug-in configuration, iSync may or may not specify device Target databases in an alert.
5.1.1. Separate Databases for Events and Tasks
The following is an example of Events and Tasks stored in separate databases:
 <?xml version="1.0"?>
 <SyncML xmlns="SYNCML:SYNCML1.1">
   <SyncHdr>
     <VerDTD>1.1</VerDTD>
     <VerProto>SyncML/1.1</VerProto>
     <SessionID>1</SessionID>
     <MsgID>1</MsgID>
     <Target>
       <LocURI>/</LocURI>
     </Target>
     <Source>
       <LocURI>iSync</LocURI>
     </Source>
   </SyncHdr>
   <SyncBody>
     <Alert>
       <CmdID>1</CmdID>
       <Data>206</Data>
       <Item>
         <Target>
           <LocURI>DeviceContacts</LocURI>
         </Target>
         <Source>
           <LocURI>Contacts</LocURI>
         </Source>
         <Meta>
           <Type xmlns="syncml:metinf">text/x-vcard</Type>
         </Meta>
       </Item>
iSync SyncML Guide 9

## 第 12 页

</Alert>
     <Alert>
       <CmdID>2</CmdID>
       <Data>206</Data>
       <Item>
         <Target>
           <LocURI>DeviceTasks</LocURI>
         </Target>
         <Source>
           <LocURI>Tasks</LocURI>
         </Source>
         <Meta>
           <Type xmlns="syncml:metinf">text/x-vcalendar</Type>
         </Meta>
       </Item>
     </Alert>
     <Alert>
       <CmdID>3</CmdID>
       <Data>206</Data>
       <Item>
         <Target>
           <LocURI>DeviceEvents</LocURI>
         </Target>
         <Source>
           <LocURI>Events</LocURI>
         </Source>
         <Meta>
           <Type xmlns="syncml:metinf">text/x-vcalendar</Type>
         </Meta>
       </Item>
     </Alert>
     <Final/>
   </SyncBody>
 </SyncML>
5.1.2. Common Database for Events and Tasks
The following is an example of Events and Tasks stored in the same database:
 <?xml version="1.0"?>
 <SyncML xmlns="SYNCML:SYNCML1.1">
   <SyncHdr>
     <VerDTD>1.1</VerDTD>
     <VerProto>SyncML/1.1</VerProto>
     <SessionID>1</SessionID>
     <MsgID>1</MsgID>
     <Target>
       <LocURI>/</LocURI>
     </Target>
     <Source>
       <LocURI>iSync</LocURI>
     </Source>
   </SyncHdr>
iSync SyncML Guide 10

## 第 13 页

<SyncBody>
     <Alert>
       <CmdID>1</CmdID>
       <Data>206</Data>
       <Item>
         <Source>
           <LocURI>Contacts</LocURI>
         </Source>
         <Meta>
           <Type xmlns="syncml:metinf">text/x-vcard</Type>
         </Meta>
       </Item>
     </Alert>
     <Alert>
       <CmdID>2</CmdID>
       <Data>206</Data>
       <Item>
         <Source>
           <LocURI>Calendars</LocURI>
         </Source>
         <Meta>
           <Type xmlns="syncml:metinf">text/x-vcalendar</Type>
         </Meta>
       </Item>
     </Alert>
     <Final/>
   </SyncBody>
 </SyncML>
5.2. SyncML 1.2 SAN example
Because iSync does not support SyncML authentication mechanism, the <digest> field is filled
with zeros.
5.2.1. Separate Databases for Events and Tasks
The following is an example of Events and Tasks stored in separate databases:
Token stream Description
00000000 00000000 00000000 00000000 digest: empty
0318000000 version: 1.2
ui-mode: 1
initiator: Server
futur-use: 0
0001 sessionid: 1
05 6953796e63 server-identifier: iSync
iSync SyncML Guide 11

## 第 14 页

Token stream Description
30 num-syncs: 3
futur-use: 0
60 sync-type: 6 (two-way by server)
futur-use: 0
000007 content-type:text/x-vcard
08 436f6e7461637473 server-uri: Contacts
60 sync-type: 6 (two-way by server)
futur-use: 0
000006 content-type:text/x-vcalendar
06 4576656e7473 server-uri: Events
60 sync-type: 6 (two-way by server)
futur-use: 0
000006 content-type:text/x-vcalendar
05 5461736b73 server-uri: Tasks
5.2.2. Common Database for Events and Tasks
The following is an example of Events and Tasks stored in the same database:
Token stream Description
00000000 00000000 00000000 00000000 digest: empty
0318000000 version: 1.2
ui-mode: 1
initiator: Server
futur-use: 0
0001 sessionid: 1
05 6953796e63 server-identifier: iSync
20 num-syncs: 2
futur-use: 0
60 sync-type: 6 (two-way by server)
futur-use: 0
000007 content-type:text/x-vcard
08 436f6e7461637473 server-uri: Contacts
iSync SyncML Guide 12

## 第 15 页

Token stream Description
60 sync-type: 6 (two-way by server)
futur-use: 0
000006 content-type:text/x-vcalendar
09 43616C656E64617273 server-uri: Calendars
iSync SyncML Guide 13

## 第 16 页

6. A Device Database Reset
iSync can detect when a user has manually reset a device's database. To do this, iSync looks at
anchors provided by the device in Pkg#1. In this case, the corresponding database on Mac is NOT
reset: instead, iSync resends all its database records to the device.
iSync considers that a device's database has been reset in following cases when a device in Pkg#1
sends one of the following alerts.
6.1. Last Anchor Is Not Present
     <Alert>
       <CmdID>3</CmdID>
       <Data>201</Data>
       <Item>
         <Target>
           <LocURI>Contacts</LocURI>
         </Target>
         <Source>
           <LocURI>DeviceContacts</LocURI>
         </Source>
         <Meta>
           <Anchor xmlns="syncml:metinf">
             <Next>1</Next>
           </Anchor>
         </Meta>
       </Item>
     </Alert>
6.2. Last Anchor Is '00000000T000000Z'
     <Alert>
       <CmdID>3</CmdID>
       <Data>201</Data>
       <Item>
         <Target>
           <LocURI>Contacts</LocURI>
         </Target>
         <Source>
           <LocURI>DeviceContacts</LocURI>
         </Source>
         <Meta>
           <Anchor xmlns="syncml:metinf">
             <Last>00000000T000000Z</Last >
             <Next>20060925T035440Z</Next>
           </Anchor>
         </Meta>
       </Item>
     </Alert>
iSync SyncML Guide 14

## 第 17 页

6.3. Last Anchor Is 0, and 'Next Anchor' Is 0
    <Alert>
       <CmdID>3</CmdID>
       <Data>201</Data>
       <Item>
         <Target>
           <LocURI>Contacts</LocURI>
         </Target>
         <Source>
           <LocURI>DeviceContacts</LocURI>
         </Source>
         <Meta>
           <Anchor xmlns="syncml:metinf">
             <Last>0</Last>
             <Next>0</Next>
           </Anchor>
         </Meta>
       </Item>
     </Alert>
6.4. Last Anchor Is 0, and 'Next Anchor' Was > 0 During
the Previous SyncML Session with That Device
•Previous session:
     <Alert>
       <CmdID>3</CmdID>
       <Data>201</Data>
       <Item>
         <Target>
           <LocURI>Contacts</LocURI>
         </Target>
         <Source>
           <LocURI>DeviceContacts</LocURI>
         </Source>
         <Meta>
           <Anchor xmlns="syncml:metinf">
             <Last>34</Last>
             <Next>35</Next>
           </Anchor>
         </Meta>
       </Item>
     </Alert>
•Session following the device's database reset:
      <Alert>
       <CmdID>3</CmdID>
       <Data>201</Data>
iSync SyncML Guide 15

## 第 18 页

<Item>
         <Target>
           <LocURI>Contacts</LocURI>
         </Target>
         <Source>
           <LocURI>DeviceContacts</LocURI>
         </Source>
         <Meta>
           <Anchor xmlns="syncml:metinf">
             <Last>0</Last>
             <Next>1</Next>
           </Anchor>
         </Meta>
       </Item>
     </Alert>
After a manual device's database is reset, if the device sends a Delete command for each record
on this database, then the corresponding database on the computer is emptied. Note that this is
not the expected behavior of a device. The device MUST NOT send a Delete command for each
record after a manual database reset.
iSync SyncML Guide 16

## 第 19 页

7. Busy Signaling
It may takes a long time for iSync to mingle data received from a SyncML client in Pkg #3. So
before starting to send Pkg #4, in order to avoid a SyncML client timeout, iSync may send one or
several Busy Signaling messages, as described in section 7.12 of [DSPRO-1.1.2].
7.1. Example of a Session with a Busy Signaling Message
•Pkg#3: iSync <= device
 <?xml version="1.0"?>
 <!DOCTYPE SyncML PUBLIC "-//SYNCML//DTD SyncML 1.1//EN" "http://www.syncml.org/
docs/syncml_represent_v11_20020213.dtd">
 <SyncML xmlns="syncml:SYNCML1.1">
   <SyncHdr>
     <VerDTD>1.1</VerDTD>
     <VerProto>SyncML/1.1</VerProto>
     <SessionID>2743</SessionID>
     <MsgID>2</MsgID>
     <Target>
       <LocURI>iSync</LocURI>
     </Target>
     <Source>
       <LocURI>IMEI:000000000000001</LocURI>
     </Source>
   </SyncHdr>
   <SyncBody>
     <Status>
       <CmdID>1</CmdID>
       <MsgRef>2</MsgRef>
       <CmdRef>0</CmdRef>
       <Cmd>SyncHdr</Cmd>
       <TargetRef>IMEI:000000000000001</TargetRef>
       <SourceRef>iSync</SourceRef>
       <Data>200</Data>
     </Status>
     <Status>
       <CmdID>2</CmdID>
       <MsgRef>2</MsgRef>
       <CmdRef>3</CmdRef>
       <Cmd>Alert</Cmd>
       <TargetRef>PhoneContact</TargetRef>
       <SourceRef>Contacts</SourceRef>
       <Data>200</Data>
       <Item>
         <Data>
           <Anchor xmlns="syncml:metinf">
             <Next>20060619T152650Z</Next>
           </Anchor>
         </Data>
       </Item>
     </Status>
     <Sync>
       <CmdID>3</CmdID>
       <Target>
         <LocURI>./Contacts</LocURI>
       </Target>
iSync SyncML Guide 17

## 第 20 页

<Source>
         <LocURI>./PhoneContact</LocURI>
       </Source>
       <Add>
         <CmdID>4</CmdID>
         <Meta>
           <Type xmlns="syncml:metinf">text/x-vcard</Type>
         </Meta>
         <Item>
           <Source>
             <LocURI>14719</LocURI>
           </Source>
           <Data><![CDATA[BEGIN:VCARD
 VERSION:2.1
 N:hi;hi;;;
 TEL;WORK:879987
 END:VCARD
 ]]></Data>
         </Item>
       </Add>
       <Add>
         <CmdID>5</CmdID>
         <Meta>
           <Type xmlns="syncml:metinf">text/x-vcard</Type>
         </Meta>
         <Item>
           <Source>
             <LocURI>14720</LocURI>
           </Source>
           <Data><![CDATA[BEGIN:VCARD
 VERSION:2.1
 N:hoho;hoho;;;
 TEL;WORK:789987
 END:VCARD
 ]]></Data>
         </Item>
       </Add>
       <Add>
         <CmdID>6</CmdID>
         <Meta>
           <Type xmlns="syncml:metinf">text/x-vcard</Type>
         </Meta>
         <Item>
           <Source>
             <LocURI>14721</LocURI>
           </Source>
           <Data><![CDATA[BEGIN:VCARD
 VERSION:2.1
 N:e;e;;;
 TEL;WORK:156651
 END:VCARD
 ]]></Data>
         </Item>
       </Add>
     </Sync>
     <Final/>
   </SyncBody>
 </SyncML>
•Pkg#4 (1): iSync => device
 <?xml version="1.0"?>
iSync SyncML Guide 18

## 第 21 页

<!DOCTYPE SyncML PUBLIC "-//SYNCML//DTD SyncML 1.1//EN" "http://www.syncml.org/
docs/syncml_represent_v11_20020213.dtd">
 <SyncML xmlns="syncml:SYNCML1.1">
   <SyncHdr>
     <VerDTD>1.1</VerDTD>
     <VerProto>SyncML/1.1</VerProto>
     <SessionID>2743</SessionID>
     <MsgID>3</MsgID>
     <Target>
       <LocURI>IMEI:000000000000001</LocURI>
     </Target>
     <Source>
       <LocURI>iSync</LocURI>
     </Source>
   </SyncHdr>
   <SyncBody>
     <Status>
       <CmdID>1</CmdID>
       <MsgRef>2</MsgRef>
       <CmdRef>0</CmdRef>
       <Cmd>SyncHdr</Cmd>
       <TargetRef>iSync</TargetRef>
       <SourceRef>IMEI:000000000000001</SourceRef>
       <Data>101</Data>
     </Status>
   </SyncBody>
 </SyncML>
•Pkg#4 (1): iSync <= device
 <?xml version="1.0"?>
 <!DOCTYPE SyncML PUBLIC "-//SYNCML//DTD SyncML 1.1//EN" "http://www.syncml.org/
docs/syncml_represent_v11_20020213.dtd">
 <SyncML xmlns="syncml:SYNCML1.1">
   <SyncHdr>
     <VerDTD>1.1</VerDTD>
     <VerProto>SyncML/1.1</VerProto>
     <SessionID>2743</SessionID>
     <MsgID>3</MsgID>
     <Target>
       <LocURI>iSync</LocURI>
     </Target>
     <Source>
       <LocURI>IMEI:000000000000001</LocURI>
     </Source>
   </SyncHdr>
   <SyncBody>
     <Alert>
       <CmdID>1</CmdID>
       <Data>221</Data>
       <Item>
         <Target>
           <LocURI>iSync</LocURI>
         </Target>
         <Source>
           <LocURI>IMEI:000000000000001</LocURI>
         </Source>
       </Item>
     </Alert>
   </SyncBody>
 </SyncML>
iSync SyncML Guide 19

## 第 22 页

•Pkg#4 (2): iSync => device
 <?xml version="1.0"?>
 <!DOCTYPE SyncML PUBLIC "-//SYNCML//DTD SyncML 1.1//EN" "http://www.syncml.org/
docs/syncml_represent_v11_20020213.dtd">
 <SyncML xmlns="syncml:SYNCML1.1">
   <SyncHdr>
     <VerDTD>1.1</VerDTD>
     <VerProto>SyncML/1.1</VerProto>
     <SessionID>2743</SessionID>
     <MsgID>4</MsgID>
     <Target>
       <LocURI>IMEI:000000000000001</LocURI>
     </Target>
     <Source>
       <LocURI>iSync</LocURI>
     </Source>
   </SyncHdr>
   <SyncBody>
     <Status>
       <CmdID>1</CmdID>
       <MsgRef>3</MsgRef>
       <CmdRef>0</CmdRef>
       <Cmd>SyncHdr</Cmd>
       <TargetRef>iSync</TargetRef>
       <SourceRef>IMEI:000000000000001</SourceRef>
       <Data>200</Data>
     </Status>
     <Status>
       <CmdID>2</CmdID>
       <MsgRef>2</MsgRef>
       <CmdRef>3</CmdRef>
       <Cmd>Sync</Cmd>
       <TargetRef>Contacts</TargetRef>
       <SourceRef>PhoneContact</SourceRef>
       <Data>200</Data>
     </Status>
     <Status>
       <CmdID>3</CmdID>
       <MsgRef>2</MsgRef>
       <CmdRef>4</CmdRef>
       <Cmd>Add</Cmd>
       <SourceRef>14719</SourceRef>
       <Data>201</Data>
     </Status>
     <Status>
       <CmdID>4</CmdID>
       <MsgRef>2</MsgRef>
       <CmdRef>5</CmdRef>
       <Cmd>Add</Cmd>
       <SourceRef>14720</SourceRef>
       <Data>201</Data>
     </Status>
     <Status>
       <CmdID>5</CmdID>
       <MsgRef>2</MsgRef>
       <CmdRef>6</CmdRef>
       <Cmd>Add</Cmd>
       <SourceRef>14721</SourceRef>
       <Data>201</Data>
     </Status>
iSync SyncML Guide 20

## 第 23 页

<Status>
       <CmdID>6</CmdID>
       <MsgRef>3</MsgRef>
       <CmdRef>1</CmdRef>
       <Cmd>Alert</Cmd>
       <Data>200</Data>
     </Status>
     <Sync>
       <CmdID>7</CmdID>
       <Target>
         <LocURI>PhoneContact</LocURI>
       </Target>
       <Source>
         <LocURI>Contacts</LocURI>
       </Source>
       <Delete>
         <CmdID>8</CmdID>
         <Item>
           <Target>
             <LocURI>14719</LocURI>
           </Target>
           <Meta>
             <Type xmlns="syncml:metinf">text/x-vcard</Type>
           </Meta>
         </Item>
       </Delete>
       <Delete>
         <CmdID>9</CmdID>
         <Item>
           <Target>
             <LocURI>14721</LocURI>
           </Target>
           <Meta>
             <Type xmlns="syncml:metinf">text/x-vcard</Type>
           </Meta>
         </Item>
       </Delete>
       <Delete>
         <CmdID>10</CmdID>
         <Item>
           <Target>
             <LocURI>14720</LocURI>
           </Target>
           <Meta>
             <Type xmlns="syncml:metinf">text/x-vcard</Type>
           </Meta>
         </Item>
       </Delete>
       <Add>
         <CmdID>11</CmdID>
         <Item>
           <Source>
             <LocURI>T-0</LocURI>
           </Source>
           <Meta>
             <Type xmlns="syncml:metinf">text/x-vcard</Type>
           </Meta>
           <Data><![CDATA[BEGIN:VCARD
 VERSION:2.1
 N:hi;hi
 TEL;WORK:879987
 END:VCARD]]></Data>
         </Item>
       </Add>
iSync SyncML Guide 21

## 第 24 页

</Sync>
     <Final/>
   </SyncBody>
 </SyncML>
7.2. Busy Signaling Not Supported
If a device doesn’t support the reception of Busy Signaling messages, then iSync may send empty
Sync commands in order to simulate Busy Signaling.
•Pkg#3: iSync <= device
 <?xml version="1.0"?>
 <!DOCTYPE SyncML PUBLIC "-//SYNCML//DTD SyncML 1.1//EN" "http://www.syncml.org/
docs/syncml_represent_v11_20020213.dtd">
 <SyncML xmlns="syncml:SYNCML1.1">
   <SyncHdr>
     <VerDTD>1.1</VerDTD>
     <VerProto>SyncML/1.1</VerProto>
     <SessionID>2745</SessionID>
     <MsgID>2</MsgID>
     <Target>
       <LocURI>iSync</LocURI>
     </Target>
     <Source>
       <LocURI>IMEI:000000000000001</LocURI>
     </Source>
   </SyncHdr>
   <SyncBody>
     <Status>
       <CmdID>1</CmdID>
       <MsgRef>2</MsgRef>
       <CmdRef>0</CmdRef>
       <Cmd>SyncHdr</Cmd>
       <TargetRef>IMEI:000000000000001</TargetRef>
       <SourceRef>iSync</SourceRef>
       <Data>200</Data>
     </Status>
     <Status>
       <CmdID>2</CmdID>
       <MsgRef>2</MsgRef>
       <CmdRef>3</CmdRef>
       <Cmd>Alert</Cmd>
       <TargetRef>PhoneContact</TargetRef>
       <SourceRef>Contacts</SourceRef>
       <Data>200</Data>
       <Item>
         <Data>
           <Anchor xmlns="syncml:metinf">
             <Next>20060619T154320Z</Next>
           </Anchor>
         </Data>
       </Item>
     </Status>
     <Sync>
       <CmdID>3</CmdID>
       <Target>
         <LocURI>./Contacts</LocURI>
       </Target>
       <Source>
         <LocURI>./PhoneContact</LocURI>
iSync SyncML Guide 22

## 第 25 页

</Source>
       <NumberOfChanges>3</NumberOfChanges>
       <Add>
         <CmdID>4</CmdID>
         <Meta>
           <Type xmlns="syncml:metinf">text/x-vcard</Type>
         </Meta>
         <Item>
           <Source>
             <LocURI>14725</LocURI>
           </Source>
           <Data><![CDATA[BEGIN:VCARD
 VERSION:2.1
 N:hi;hi;;;
 TEL;WORK:879987
 END:VCARD
 ]]></Data>
         </Item>
       </Add>
       <Add>
         <CmdID>5</CmdID>
         <Meta>
           <Type xmlns="syncml:metinf">text/x-vcard</Type>
         </Meta>
         <Item>
           <Source>
             <LocURI>14726</LocURI>
           </Source>
           <Data><![CDATA[BEGIN:VCARD
 VERSION:2.1
 N:hoho;hoho;;;
 TEL;WORK:789987
 END:VCARD
 ]]></Data>
         </Item>
       </Add>
       <Add>
         <CmdID>6</CmdID>
         <Meta>
           <Type xmlns="syncml:metinf">text/x-vcard</Type>
         </Meta>
         <Item>
           <Source>
             <LocURI>14727</LocURI>
           </Source>
           <Data><![CDATA[BEGIN:VCARD
 VERSION:2.1
 N:e;e;;;
 TEL;WORK:156651
 END:VCARD
 ]]></Data>
         </Item>
       </Add>
     </Sync>
     <Final/>
   </SyncBody>
 </SyncML>
•Pkg#3: iSync <= device
 <?xml version="1.0"?>
iSync SyncML Guide 23

## 第 26 页

<!DOCTYPE SyncML PUBLIC "-//SYNCML//DTD SyncML 1.1//EN" "http://www.syncml.org/
docs/syncml_represent_v11_20020213.dtd">
 <SyncML xmlns="syncml:SYNCML1.1">
   <SyncHdr>
     <VerDTD>1.1</VerDTD>
     <VerProto>SyncML/1.1</VerProto>
     <SessionID>2745</SessionID>
     <MsgID>3</MsgID>
     <Target>
       <LocURI>IMEI:000000000000001</LocURI>
     </Target>
     <Source>
       <LocURI>iSync</LocURI>
     </Source>
   </SyncHdr>
   <SyncBody>
     <Status>
       <CmdID>1</CmdID>
       <MsgRef>2</MsgRef>
       <CmdRef>0</CmdRef>
       <Cmd>SyncHdr</Cmd>
       <TargetRef>iSync</TargetRef>
       <SourceRef>IMEI:000000000000001</SourceRef>
       <Data>200</Data>
     </Status>
     <Status>
       <CmdID>2</CmdID>
       <MsgRef>2</MsgRef>
       <CmdRef>3</CmdRef>
       <Cmd>Sync</Cmd>
       <TargetRef>Contacts</TargetRef>
       <SourceRef>PhoneContact</SourceRef>
       <Data>200</Data>
     </Status>
     <Status>
       <CmdID>3</CmdID>
       <MsgRef>2</MsgRef>
       <CmdRef>4</CmdRef>
       <Cmd>Add</Cmd>
       <SourceRef>14725</SourceRef>
       <Data>201</Data>
     </Status>
     <Status>
       <CmdID>4</CmdID>
       <MsgRef>2</MsgRef>
       <CmdRef>5</CmdRef>
       <Cmd>Add</Cmd>
       <SourceRef>14726</SourceRef>
       <Data>201</Data>
     </Status>
     <Status>
       <CmdID>5</CmdID>
       <MsgRef>2</MsgRef>
       <CmdRef>6</CmdRef>
       <Cmd>Add</Cmd>
       <SourceRef>14727</SourceRef>
       <Data>201</Data>
     </Status>
     <Sync>
       <CmdID>6</CmdID>
       <Target>
         <LocURI>PhoneContact</LocURI>
       </Target>
       <Source>
iSync SyncML Guide 24

## 第 27 页

<LocURI>Contacts</LocURI>
       </Source>
     </Sync>
   </SyncBody>
 </SyncML>
•Pkg#3: iSync <= device
 <?xml version="1.0"?>
 <!DOCTYPE SyncML PUBLIC "-//SYNCML//DTD SyncML 1.1//EN" "http://www.syncml.org/
docs/syncml_represent_v11_20020213.dtd">
 <SyncML xmlns="syncml:SYNCML1.1">
   <SyncHdr>
     <VerDTD>1.1</VerDTD>
     <VerProto>SyncML/1.1</VerProto>
     <SessionID>2745</SessionID>
     <MsgID>3</MsgID>
     <Target>
       <LocURI>iSync</LocURI>
     </Target>
     <Source>
       <LocURI>IMEI:000000000000001</LocURI>
     </Source>
   </SyncHdr>
   <SyncBody>
     <Alert>
       <CmdID>1</CmdID>
       <Data>222</Data>
       <Item>
         <Target>
           <LocURI>iSync</LocURI>
         </Target>
         <Source>
           <LocURI>IMEI:000000000000001</LocURI>
         </Source>
       </Item>
     </Alert>
     <Status>
       <CmdID>2</CmdID>
       <MsgRef>3</MsgRef>
       <CmdRef>0</CmdRef>
       <Cmd>SyncHdr</Cmd>
       <TargetRef>IMEI:000000000000001</TargetRef>
       <SourceRef>iSync</SourceRef>
       <Data>200</Data>
     </Status>
     <Status>
       <CmdID>3</CmdID>
       <MsgRef>3</MsgRef>
       <CmdRef>6</CmdRef>
       <Cmd>Sync</Cmd>
       <TargetRef>PhoneContact</TargetRef>
       <SourceRef>Contacts</SourceRef>
       <Data>200</Data>
     </Status>
   </SyncBody>
 </SyncML>
•Pkg#3: iSync <= device
iSync SyncML Guide 25

## 第 28 页

<?xml version="1.0"?>
 <!DOCTYPE SyncML PUBLIC "-//SYNCML//DTD SyncML 1.1//EN" "http://www.syncml.org/
docs/syncml_represent_v11_20020213.dtd">
 <SyncML xmlns="syncml:SYNCML1.1">
   <SyncHdr>
     <VerDTD>1.1</VerDTD>
     <VerProto>SyncML/1.1</VerProto>
     <SessionID>2745</SessionID>
     <MsgID>4</MsgID>
     <Target>
       <LocURI>IMEI:000000000000001</LocURI>
     </Target>
     <Source>
       <LocURI>iSync</LocURI>
     </Source>
   </SyncHdr>
   <SyncBody>
     <Status>
       <CmdID>1</CmdID>
       <MsgRef>3</MsgRef>
       <CmdRef>0</CmdRef>
       <Cmd>SyncHdr</Cmd>
       <TargetRef>iSync</TargetRef>
       <SourceRef>IMEI:000000000000001</SourceRef>
       <Data>200</Data>
     </Status>
     <Status>
       <CmdID>2</CmdID>
       <MsgRef>3</MsgRef>
       <CmdRef>1</CmdRef>
       <Cmd>Alert</Cmd>
       <Data>200</Data>
     </Status>
     <Sync>
       <CmdID>3</CmdID>
       <Target>
         <LocURI>PhoneContact</LocURI>
       </Target>
       <Source>
         <LocURI>Contacts</LocURI>
       </Source>
       <NumberOfChanges>4</NumberOfChanges>
       <Delete>
         <CmdID>4</CmdID>
         <Item>
           <Target>
             <LocURI>14727</LocURI>
           </Target>
           <Meta>
             <Type xmlns="syncml:metinf">text/x-vcard</Type>
           </Meta>
         </Item>
       </Delete>
       <Delete>
         <CmdID>5</CmdID>
         <Item>
           <Target>
             <LocURI>14726</LocURI>
           </Target>
           <Meta>
             <Type xmlns="syncml:metinf">text/x-vcard</Type>
           </Meta>
         </Item>
       </Delete>
iSync SyncML Guide 26

## 第 29 页

<Delete>
         <CmdID>6</CmdID>
         <Item>
           <Target>
             <LocURI>14725</LocURI>
           </Target>
           <Meta>
             <Type xmlns="syncml:metinf">text/x-vcard</Type>
           </Meta>
         </Item>
       </Delete>
       <Add>
         <CmdID>7</CmdID>
         <Item>
           <Source>
             <LocURI>T-0</LocURI>
           </Source>
           <Meta>
             <Type xmlns="syncml:metinf">text/x-vcard</Type>
           </Meta>
           <Data><![CDATA[BEGIN:VCARD
 VERSION:2.1
 N:hi;hi
 TEL;WORK:879987
 END:VCARD]]></Data>
         </Item>
       </Add>
     </Sync>
      <Final/>
   </SyncBody>
 </SyncML>
7.3. Only One Busy Signaling Message Is Supported
If a device supports the reception of only one Busy Signaling message, then iSync sends a Busy
Signaling message first, followed by empty Sync commands.
iSync SyncML Guide 27

## 第 30 页

8. Databases
iSync supports only the vCard 2.1 and vCal 1.0 formats.
iSync can synchronize these databases:
•Contacts
•Events
•Tasks
iSync works with devices that have a common database for Events and Tasks, as well as with
those that have separate databases for Events and Tasks.
8.1. vCard
Any client that supports SyncML contact sync, MUST use vCard 2.1 to convey contact information.
8.1.1. Supported Fields
The following table corresponds to the mapping between the Address Book fields that can be
synced by iSync, and the default vCard properties used to sync them.
Address Book field vCard PropertyMultiple values
allowed
Street / Postal Code / City / Country ADR (or LABEL) X
Birthday BDAY
Email EMAIL X
First / Last / Middle Name / Prefix / Suffix N
Note NOTE
Company / Department ORG
Photo PHOTO
Phone TEL X
Job Title TITLE
URL URL X
Nickname X-NICKNAME
Dates : Anniversary X-ANNIVERSARYX
iSync SyncML Guide 28

## 第 31 页

Address Book field vCard PropertyMultiple values
allowed
Dates : Custom X-DATE X
Related Names: Father X-FATHER X
Related Names: Mother X-MOTHER X
Related Names: Parent X-PARENT X
Related Names: Child X-CHILD X
Related Names: Brother X-BROTHER X
Related Names: Sister X-SISTER X
Related Names: Friend X-FRIEND X
Related Names: Spouse X-SPOUSE X
Related Names: Assistant X-ASSISTANT X
Related Names: Manager X-MANAGER X
Related Names: Other / Custom X-NAME X
8.1.2. Type Mapping
The following tables in this section correspond to ideal TYPE parameter mappings.
8.1.2.1. Delivery address (ADR)
Address Book type vCard type
work WORK
home HOME
other / custom (none)
8.1.2.2. Email (EMAIL)
Address Book type vCard type
work WORK
home HOME
iSync SyncML Guide 29

## 第 32 页

Address Book type vCard type
other / custom (none)
8.1.2.3. Phone (TEL)
Address Book type vCard type
work WORK
home HOME
mobile CELL
main (none)
home fax HOME;FAX
work fax WORK;FAX
pager PAGER
other / custom (none)
8.1.2.4. URL (URL)
Address Book type vCard type
home page HOME
work WORK
home HOME
other / custom (none)
8.2. vCal
Any client supporting a SyncML event or task sync, MUST use vCal 1.0 to convey event or task
information.
8.2.1. Supported Fields
The following table corresponds to the mapping between the iCal fields that can be synced by
iSync, and the vCal properties used to sync them.
iSync SyncML Guide 30

## 第 33 页

iCal field vCal Property
From DTSTART
To DTEND
Title SUMMARY
Location LOCATION
Notes DESCRIPTION
Alarm [Message] DALARM
Alarm [Message with sound] AALARM
Repeat RRULE / EXDATE
Priority PRIORITY
Due date DUE
Completed COMPLETED
(hidden) STATUS
(hidden) CLASS
8.2.2. All Day Event
SyncML client is said to support All Day events if:
•A user can set an event as All Day on device's UI.
•The All Day information is sent by the device in the associated vCal during the sync session.
iSync supports several All Day event formats.
8.2.2.1. OMA Formatting
If a device supports  synchronization of All Day Events, it SHOULD represent them as described in
[VOBJPROFILE-1.0].
•Single day:
 BEGIN:VCALENDAR
 VERSION:1.0
 BEGIN:VEVENT
 DTSTART:20060925T000000
 DTEND:20060925T240000
 SUMMARY:This is an allday event (on 09/25/06)
 END:VEVENT
iSync SyncML Guide 31

## 第 34 页

END:VCALENDAR
•Multi day:
 BEGIN:VCALENDAR
 VERSION:1.0
 BEGIN:VEVENT
 DTSTART:20060925T000000
 DTEND:20060926T240000
 SUMMARY:This is an allday event (from 09/25/06 to 09/26/06)
 END:VEVENT
 END:VCALENDAR
8.2.2.2. From Midnight to Midnight (the day after)
•Single day:
 BEGIN:VCALENDAR
 VERSION:1.0
 BEGIN:VEVENT
 DTSTART:20060925T000000
 DTEND:20060926T000000
 SUMMARY:This is an allday event (on 09/25/06)
 END:VEVENT
 END:VCALENDAR
•Multi day:
 BEGIN:VCALENDAR
 VERSION:1.0
 BEGIN:VEVENT
 DTSTART:20060925T000000
 DTEND:20060927T000000
 SUMMARY:This is an allday event (from 09/25/06 to 09/26/06)
 END:VEVENT
 END:VCALENDAR
8.2.2.3. Using the CATEGORIES property
Phone plug-in developers must explicitly specify the CATEGORIES values for which a device
considers an event to be All Day, and for which a device considers an event to be Timed.
•Single day:
 BEGIN:VCALENDAR
 VERSION:1.0
 BEGIN:VEVENT
 CATEGORIES:REMINDER
 DTSTART:20060925T150000
 DTEND:20060925T150000
iSync SyncML Guide 32

## 第 35 页

SUMMARY:This is an allday event (on 09/25/06)
 END:VEVENT
 END:VCALENDAR
•Multi day:
 BEGIN:VCALENDAR
 VERSION:1.0
 BEGIN:VEVENT
 CATEGORIES:REMINDER
 DTSTART:20060925T150000
 DTEND:20060926T150000
 SUMMARY:This is an allday event (from 09/25/06 to 09/26/06)
 END:VEVENT
 END:VCALENDAR
8.2.2.4. From Midnight to 23:59
•Single day:
 BEGIN:VCALENDAR
 VERSION:1.0
 BEGIN:VEVENT
 DTSTART:20060925T000000
 DTEND:20060925T235900
 SUMMARY:This is an allday event (on 09/25/06)
 END:VEVENT
 END:VCALENDAR
•Multi day:
 BEGIN:VCALENDAR
 VERSION:1.0
 BEGIN:VEVENT
 DTSTART:20060925T000000
 DTEND:20060926T235900
 SUMMARY:This is an allday event (from 09/25/06 to 09/26/06)
 END:VEVENT
 END:VCALENDAR
8.2.3. Recurrences Rules
•Only one RRULE property per vCal is supported.
•RRULE is supported only on VEVENT, not on VTODO.
iSync SyncML Guide 33
