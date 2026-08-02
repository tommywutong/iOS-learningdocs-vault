---
title: Changing the Default Directory for StandardFile Calls
apple_id: DTS10002201
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/tb/tb15.html
archived_at: '2026-07-18T02:38:56.040531Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TB15Changing the Default Directory for StandardFile Calls |

|  |
| --- |
| Q I have been using the StandardFile calls, such as CustomGetFile, CustomPutFile, and so on and changed the directory that they default to. I accomplish this by getting the current parID and vRefNum and then switching to the folder and volume I want presented to the user. I do this by calling routines that I developed which set low-memory globals. I am now using the Apple-developed calls, LMGetCurDirStore(), LMPutCurDirStore(), LMGetCurApRefNum(), and LMPutCurApRefNum(), and I'm having difficulty getting the StdFile calls to accept a directory change. It appears that the General Controls panel also has options that can affect which directory is defaulted to.  I want to force the user to see only the directory I present to them. I use a my own application preferences folder under the System Preferences folder as the home for any document created by my application. Therefore, regardless of the General Control settings, I want to go to a specific directory anytime users access the New or Open file menu items.  What is the proper sequence of calls to accomplish this? A The changes you observed in the StandardFile dialogs with regard to the use of the low memory global CurDirStore are the result of a patch we added to the General Controls control panel of System 7.5. This patch was implemented to allow users to control the default directory. With this patch, users can change the behavior of System 7.5 so it is the same as it was under System 7.0 and 7.1. To do this, they open the General Controls control panel, and under Documents, choose "When opening or saving a document, take me to", then choose "Folder which contains the application".  Obviously, this user-centered solution is not ideal in your situation. There is one way you can override this new "feature" of System 7.5 programmatically to allow your application to set the default directory used by StandardFile.  The workaround is to use CustomGetFile and set up a dialog hook, filling in the values in the information sent to the dialog hook before you call CustomGetFile. This method is preferable to ensure that your application is compatible with future revisions of the System software. The code below gets the vRefNum and dirID of the System's Preferences Folder and defaults to using this location each time CustomGetFile is called. You should be able to use this on any system which uses CustomGetFile to set up the default directory before calling CustomGetFile.   ``` /* dialog hook workaround */  typedef struct {    StandardFileReply *replyPtr;    FSSpec oldSelection; } SFData, *SFDataPtr;  DlgHookYDUPP gDlgHookYDUPP;  pascal short MyDlgHook(short item,DialogPtr theDialog,Ptr myDataPtr)  {  SFDataPtr            sfUserData;    short                foundVRefNum;    long                 foundDirID, refcon;    OSErr                myErr;     /* only for the main dialog box */    refcon = GetWRefCon(theDialog);    if (refcon != sfMainDialogRefCon)    return item;    sfUserData = (SFDataPtr) myDataPtr;     if (item==sfHookFirstCall)      {    return sfHookChangeSelection;     }       return item;     }   void TestNewStandardFile ()  {   SFReply reply;    DialogPtr theDialog;    short item;    StandardFileReply sfReply;    SFData sfUserData;    OSErr err;    Point where = {-1,-1};    short        foundVRefNum;    long         foundDirID, refcon;      sfUserData.replyPtr = &sfReply;     err = FindFolder(kOnSystemDisk, kPreferencesFolderType, kDontCreateFolder,                       &foundVRefNum, &foundDirID);     sfUserData.replyPtr -> sfFile.parID   = foundDirID;    sfUserData.replyPtr -> sfFile.vRefNum = foundVRefNum;     /* just display a custom get file dialog defaulted to the */    /* preferences folder dirID and vRefNum in the dialog hook */     CustomGetFile(nil,-1,nil,&sfReply,700,where,gDlgHookYDUPP,    nil,nil,nil,&sfUserData);  }   gDlgHookYDUPP = NewDlgHookYDProc(MyDlgHook);  /* end of dialog hook workaround */ ```   This code sample is a slightly modified version of the dialog-hook example on page 3-33 of _Inside Macintosh:Files_. Instead of coding the default directory into the dialog hook, this code passes the desired target directory information to the Dialog Hook function through the myDataPtr parameter. This allows you to default to different directories, depending on which part of your program is using the Dialog Hook. For example, you might want to have CustomGetFile() default to your Preferences Folder, while CustomPutFile() defaults to the Desktop Folder. You can use the same Dialog Hook as long as you supply the volume reference number and the directory ID before calling CustomGetFile/CustomPutFile, and you don't have to manipulate low-memory globals by calling LMSetCurDirStore and LMSetSFSaveDisk, if you use this technique.  This code works by first obtaining the vRefNum and the dirID for the Preferences folder via the FindFolder call. Then, it assigns the volume reference number and the directory ID to sfUserData. When it calls CustomGetFile(), it includes the address of sfUserData as the last parameter (this is the key to the procedure). When CustomGetFile calls the DialogHook routine, it passes this sfUserData pointer on the stack, making the volume-reference number and the directory ID obtained with the FindFolder call available to the DialogHook.  In the Dialog Hook function, the sfHookFirstCall constant is a pseudo-item that Standard File sends to your dialog-hook function immediately before it displays the CustomGetFile dialog box. The dialog-hook function responds to this pseudo-item by returning the pseudo-item sfHookChangeSelection. When your application returns this pseudo-item, it is telling Standard File that it wants it to change the Standard File reply record so that it describes the target folder you passed in the myDataPtr field.  This technique is fairly well-documented on pages 3-21 through 3-40 of _Inside Macintosh:Files._ Another sample that uses this technique is SettingUpStdFile, which is on the Tool Chest Edition of the Developer CD.  Don't rely heavily on this technique: the user might not expect the directory set for standard file to override their preferences set in the general control panel. There is also no guarantee that this workaround will continue to work with future versions of system software. [Jun 01 1995] |

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
