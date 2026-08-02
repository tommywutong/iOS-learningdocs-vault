---
title: Supporting Printing in Your Carbon Application
apple_id: TP30000978
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2004-08-31'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/CPM_Concepts/cpm_chap3/cpm_tasks.html
archived_at: '2026-07-15T05:22:31.346055Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Supporting Printing in Your Carbon Application](Introduction%20to%20Supporting%20Printing%20in%20Your%20Carbon%20Application.md)


[Next](Adopting%20the%20Carbon%20Printing%20Manager.md)[Previous](Printing%20Concepts%20for%20Carbon%20Developers.md)

# Printing Tasks

[Chapter 2, Printing Concepts for Carbon Developers,](Printing%20Concepts%20for%20Carbon%20Developers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambuguwviubz) discussed the high-level tasks required to support printing in a Carbon application: setting up the page format, setting up the print settings, and printing the print job. This chapter shows you how to implement each of those tasks for a document-based Carbon application, such as a text editor or drawing application. This chapter describes the following tasks:

- [Setting Up the Page Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummrt). Your application must make sure valid page format settings exist for a document.
- [Setting Up the Print Settings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummru). Your application must make sure valid print settings exist for a print job.
- [Printing the Job](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywueqkki5auercb). Your application must determine how many pages are in the print job and draw each page.
- [Handling Errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummju). Errors can occur at many points during the printing process. Your application should provide a function to post error messages, should they occur.
- [Saving a Document as a PDF File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywueqkki5cueske). Saving a document as a portable document format (PDF) file in Mac OS X uses code similar to the code you need to print a document to a printer. With very little effort on your part, your application can provide users with the ability to save their documents to a file that uses this popular format.
- [Printing One Copy](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywueqkkivbukrkj). Your application can provide a shortcut command (Print One Copy) to allow users to print a single copy of a document using default settings without requiring them to open the Page Setup and Print dialogs.
- [Printing Multiple Copies](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywueq2ji5cugqkj). The printing system handles printing multiple copies for you.

This chapter contains sample code to illustrate each task you need to do to support printing. See [Printing Carbon Sample Code](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP30000432-TP30000494) for the sample application on which the code is based.

If you’ve installed the Mac OS X Developer Tools CD you can find additional sample applications in the following directory that show how to support printing in Mac OS X. You can compile and run the sample applications in Project Builder.

`/Developer/Examples/Printing/App/`

As you go through the sample code in this chapter, note that any function, data type, or constant your application must supply has the prefix `My`, except for global constants, which use the prefix `gMy`. Application-defined constants have the prefix `kMy`. Carbon Printing Manager functions use the prefix `PM.` If a line of code contains a commented number, an explanation for that line of code follows the listing.

Most Carbon applications that print allow the user to choose the Page Setup command from the File menu to set options that control the page format for a document. This section shows you how to set up the page format in response to the Page Setup command. It discusses the following tasks that your application needs to perform to set up the page format for a document:

- [Responding to the Page Setup Command](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcumny)
- [Setting Up a Page Format Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywueqkki5bucskc)
- [Handling Dismissal of the Page Setup Dialog](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywueqkkjjcekrsk)

This section also shows how to flatten page format data so you can save it with a document and unflatten saved data to use it. See [Saving and Retrieving Page Format Data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummjx) for information on how to perform these optional tasks.

When the user chooses Page Setup from the File menu your application needs to perform the following operations:

1. Create a printing session object.
2. Make sure there is a valid page format object for the document by performing one of the following actions:

   If no page format object exists for the document, your application must create one and set it to default values for this session. (The page format object is not usable until it has default values.)

   If the page format object already exists, validate the object against the printing session object. Validation updates any fields in the page format object that need to be calculated, such as the adjusted page and paper rectangles.

   If the page format object doesn’t exist, but the document has page format data saved with it, your application needs to unflatten the saved data to create a page format object that contains the saved settings.
3. Call the function`PMSessionUseSheets` to indicate that the Page Setup dialog should use sheets. Although sheets are not available in Mac OS 9 and earlier, you should call this function if your application runs in Mac OS X as well as Mac OS 9. In Mac OS 9, the function returns a result code that indicates sheets are not available.
4. Call `PMSessionPageSetupDialog` to display the Page Setup dialog so the user can specify settings such as paper size and orientation. In Mac OS X, the dialog is displayed as a sheet as long as you called the function `PMSessionUseSheets`.
5. Preserve page setup information. Users expect page setup information to persist with the document. Your application should save the page format data with the document.
6. Release the printing session object and handle errors, if any occur.

One of the major design decisions you must make for your application is how to handle the page format object for the document. The page format should persist with the document after the user has dismissed the Page Setup dialog. In other words, the next time the user opens the Page Setup dialog for the document, the settings should be the same as they were when the user last closed the Page Setup dialog for that document. The settings should persist when the user quits the application, launches it again, and then opens the document.

There are a variety of ways you can handle page format data for a document. The sample code in this chapter stores the page format object in a structure and attaches it to a document window as a property. The structure is simple; it contains only two items. Most document-based applications use a larger structure to store all information about the document, including printing-related information. You need to handle the page format data in a way that’s best for your application.

The sample code assumes the following structure is defined:

```
typedef struct MyDocData
{
    PMPageFormat             pageFormat;
    PMPrintSettings          printSettings;
}MyDocData;
```

The structure `MyDocData` contains two fields, one of type `PMPageFormat` and another of type `PMPrintSettings`. Although it is important for the page format data to persist with the document, it is not recommended that print settings data persist. However, as you’ll see in [Setting Up the Print Settings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummru), using the structure `MyDocData` provides a convenient way to pass the print settings object from one function to another; the print settings are not saved with the document after the print job is cancelled or sent to a print queue.

The function `MyDoPageSetup` in [Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummjqgy) shows how your application can respond to the Page Setup command. Following this listing is a detailed explanation for each line of code that has a numbered comment.

__Listing 2-1__  A function that responds to the Page Setup command


```
OSStatus MyDoPageSetup (WindowRef documentWindow,
                            MyDocData *docDataP)// 1
{
    OSStatus err = noErr;

    if (docDataP)// 2
    {
        PMPrintSession printSession;
        PMPageFormat pageFormat = NULL;
        err = PMCreateSession (&printSession);// 3
        if (!err)
         {
            Boolean accepted;
            err = MySetupPageFormatForPrinting (printSession,
                                            docDataP, &pageFormat);// 4
            if (!err)
             {
                Boolean sheetsAreAvailable = true;// 5
                err = PMSessionUseSheets (printSession, documentWindow,
                                            gMyPageSetupDoneProc); // 6
                if (err == kPMNotImplemented)// 7
                {
                        err = noErr;
                        sheetsAreAvailable = false;
                }
                if (!err)
                {
                     err = PMSessionPageSetupDialog (printSession,
                                pageFormat, &accepted);// 8
                    if (err == noErr && !sheetsAreAvailable)
                    MyPageSetupDoneProc (printSession,
                                            window, accepted);// 9
                }
            }
            if (err)
                (void) PMRelease (printSession);// 10
        }
    }
    MyPostPrintingError (err, kMyPrintErrorFormatStrKey);// 11
    return err;
}
```

Here’s what the code in [Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummjqgy) does:

1. Passes a reference to the document window and a pointer to the data structure that contains the page format object (`PMPageFormat`) for the document. Your application can get the pointer (`docDataP`) to pass to your `MyDoPageSetup` function by calling the Window Manager function `GetWindowProperty`. This assumes that you have already set up the data structure and set it as a property of the window using the Window Manager function `SetWindowProperty`.
2. Makes sure the pointer is valid.
3. Calls the Carbon Printing Manager function `PMCreateSession` to create a printing session object that is used for the page format code that follows.
4. Calls your application’s function to set up a page format object. See [Setting Up a Page Format Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywueqkki5bucskc). Pass the printing session, the pointer to the structure `MyDocData`, and a pointer to the local page format object.
5. Sheets are not available in Mac OS 8 and 9. If you plan to run your application in Mac OS 8 and 9 as well as in Mac OS X, you need to write your code so it acts properly in both situations. This code demonstrates how you can support each operating system. First, create a variable `sheetsAreAvailable` and set it to `true`.
6. Calls the Carbon Printing Manager function `PMSessionUseSheets` to specify that a printing dialog (in this case the Page Setup dialog) should be displayed as a sheet.

   You need to pass the current printing session, the window that contains the document to be printed, and a pointer to your page setup done function. When using sheets in Mac OS X, the Carbon Printing Manager calls your function when the user dismisses the Page Setup dialog. This code assumes the application already declared a global variable:

```
gMyPageSetupDoneProc = NewPMSheetDoneUPP (MyPageSetupDoneProc);
```

   If your application runs in Mac OS 8 or 9, calling the function `PMSessionUseSheets` returns the error `kPMNotImplemented`, and the function has no effect.
7. Checks for the error `kPMNotImplemented`. If it is returned, that means your application is running in Mac OS 8 or 9, and that you are responsible for calling your procedure to handle dismissal of the Page Setup dialog. Set the constant `sheetsAreAvailable` to `false`.
8. Calls the Carbon Printing Manager function `PMSessionPageSetupDialog` to display the Page Setup dialog. Pass the current printing session, the page format object that was set up in a previous step, and a pointer to a Boolean value. You call this function regardless of the version of the operating system. If your application is running in Mac OS X, the dialog appears as a sheet.

   The following is true if you are using sheets:

   - When the user dismisses the Page Setup dialog, the Carbon Printing Manager calls the function specified by the constant `gMyPageSetupDoneUPP` in the previous call to `PMSessionUseSheets`.
   - When using sheets, the `PMSessionPageSetupDialog` function returns immediately and the Boolean value returned in the `accepted` parameter is irrelevant because it is your Page Setup dialog done function that is called when the dialog is dismissed. If your application needs to perform additional tasks after the user dismisses the Page Setup dialog, it can do so in the `MyPageSetupDoneProc` function, which is called when the user dismisses the Page Setup dialog.
   - If the user clicks the OK button in the Page Setup dialog, the page format object is updated with the user’s changes (if any) and the value `true` is returned to the `MyPageSetupDoneProc` function. If the user clicks the Cancel button, the page format object is unchanged and the value `false` is returned to the `MyPageSetupDoneProc` function.

   The following is true if you are not using sheets:

   - The `PMSessionPageSetupDialog` function does not return until the user dismisses the Page Setup dialog.
   - The Boolean value returned in the `accepted` variable is `true` if the user clicks OK and `false` if the user clicks Cancel.
9. If there is no error, and sheets are not available, then your application must call its Page Setup dialog done function (`MyPageSetupDoneProc`) to process the results of the Page Setup dialog and do any necessary clean up.
10. If an error is returned from the Page Setup dialog or prior to showing the dialog, then you must release the printing session here. Otherwise you should release the printing session in your Page Setup dialog done function (`MyPageSetupDoneProc`).
11. Calls your application’s function to display an error message. See [Handling Errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummju) for more information. If there is no error, the function does nothing.

The function `MySetupPageFormatForPrinting`, shown in [Listing 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywueqkkizduurkc), makes sure there is a valid page format object for a document. The advantage to creating a separate function to take care of the page format object is that your application can call the function when it handles the Page Setup command and when it handles the Print command. [Responding to the Print Command](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywueqkkinfegscc) describes how to handle the Print command.

__Listing 2-2__  A function that sets up a page format object


```swift
static OSStatus MySetupPageFormatForPrinting (
                                PMPrintSession printSession,
                                MyDocData *docDataP,
                                PMPageFormat *pageFormatP)// 1
{
    OSStatus status = noErr;
    PMPageFormat pageFormat = docDataP->pageFormat;// 2
    if (pageFormat == NULL)// 3
    {
        status = PMCreatePageFormat (&pageFormat);
        if (status == noErr)
        {
            status = PMSessionDefaultPageFormat (printSession,
                                                pageFormat);
            if (status == noErr)
                docDataP->pageFormat = pageFormat;
            else
             {
                (void) PMRelease (pageFormat);
                pageFormat = NULL;
            }
        }
    }
    else// 4
    {
        status = PMSessionValidatePageFormat (printSession, pageFormat,
                                        kPMDontWantBoolean);
        if (status)
        {
            docDataP->pageFormat = NULL;
            (void) PMRelease (pageFormat);
            pageFormat = NULL;
        }
    }

    *pageFormatP = pageFormat;// 5
    return status;
}
```

Here’s what the code does:

1. Passes the current printing session object (created either in `MyDoPageSetup` or `MyDoPrint`), a pointer to the `MyDocData` structure, and a pointer to a page format object (created either in `MyDoPageSetup` or `MyDoPrint`).
2. Declares a local variable to hold a page format object and set its value to the document’s page format.
3. If the local page format is `NULL`, calls the Carbon Printing Manager function `PMCreatePageFormat` to allocate the page format object, and then do the following:

   - Sets the newly allocated page format object to default values by calling the Carbon Printing Manager function `PMSessionDefaultPageFormat`.
   - If setting up defaults for the local page format object is successful, then sets the document’s page format object to the local page format object. If it isn’t successful, you need to release the local page format object and set it to `NULL`.
4. If the local page format is not `NULL`, then validates the local page format object within the context of the current printing session. Validating updates any values in the page format object that need to be calculated, such as the adjusted page and paper rectangles.

   If the validation does not succeed, you need to set the document’s page format object to `NULL`, release the local page format object, and set the local page format object to `NULL`.
5. If the code is successful so far, you need to assign the local page format object to the storage (`pageFormatP`) you passed to your `MySetupPageFormatForPrinting` function.

You need to provide a function to handle dismissal of the Page Setup dialog. If your application uses sheets, the Carbon Printing Manager calls this function when the user dismisses the Page Setup dialog. Otherwise, your application needs to call this function.

At a minimum this function should release the current printing session object, which shouldn’t be saved after the user dismisses the Page Setup dialog. If your application has more complicated printing needs, it may need to include code to perform other operations here. For example, your application may need to reformat pages to reflect changes the user made to scaling or paper size options in the Page Setup dialog.

The function `MyPageSetupDoneProc` in [Listing 3-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywueqkdjfdusrsh) shows how you can handle dismissal of the Page Setup dialog in your application. The function takes three parameters: the current printing session object, a reference to the document window, and a Boolean to indicate whether the user accepted or cancelled the Page Setup dialog. The function does two things: releases the printing session object and calls your application’s function to post a printing error, should one occur. See [Handling Errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummju) for information on the error-posting function.

__Listing 2-3__  A function to handle dismissal of the Page Setup dialog


```
static pascal void MyPageSetupDoneProc (PMPrintSession printSession,
                        WindowRef documentWindow,
                        Boolean accepted)
{
    #pragma unused (documentWindow, accepted)

    OSStatus err = PMRelease (printSession);
    if (err)
        MyPostPrintingError (err, kMyPrintErrorFormatStrKey);
    return;
}
```


When the user saves a document, most applications save the page format data with it, which consists of choices made by the user in the Page Setup dialog. Because a page format object is an opaque data type, you need to flatten the object before you can save it. When you want to use the data, you need to unflatten it to restore the original page format object.

[Listing 3-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywueqkkineusr2d) shows an example of how you can flatten a page format object so it can be saved with the document. The `MyFlattenAndSavePageFormat` function assumes the caller passes a validated page format object. The function `PMFlattenPageFormat` flattens a page format object to a handle before the application writes it to a document or other location.

__Listing 2-4__  Saving page format data


```
OSStatus MyFlattenAndSavePageFormat (PMPageFormat pageFormat)
{
    OSStatus    status = noErr;
    Handle      flatFormatHandle = NULL;

    if (pageFormat != kPMNoPageFormat)
    {
         status = PMFlattenPageFormat (pageFormat, &flatFormatHandle);
         if (status == noErr)
            //  In this sample code we simply put it in a global variable.
            //  Replace this line with your code to write the data to a file.
            gflatPageFormat = flatFormatHandle;
    }
    return status;
}
```

[Listing 3-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywuerkjirbuqrcb) shows a function—`MyLoadAndUnflattenPageFormat`—that gets flattened page format data and returns a page format object. The function `PMUnFlattenPageFormat` converts the flattened data to a page format object.

__Listing 2-5__  Retrieving page format data


```

OSStatus    MyLoadAndUnflattenPageFormat (PMPageFormat* pageFormat)
{
    OSStatus    status;
    Handle  flatFormatHandle = NULL;

    //  This sample code copies flattened data from a global.
    //  Replace this line with your code to obtain the flattened data
    //  from your document.
    flatFormatHandle = gflatPageFormat;
    status = PMUnflattenPageFormat (flatFormatHandle, pageFormat);

    return status;
}
```


Most Carbon applications that support printing allow the user to choose Print from the File menu to set options that control how a document is printed. This section shows you how to respond to the Print command issued when the user chooses Print from the File menu. It discusses the following tasks that your application needs to do to set up print settings for a document:

- [Responding to the Print Command](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywueqkkinfegscc)
- [Handling Dismissal of the Print Dialog](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummrq)

The sample code assumes the following structure is defined:

```
typedef struct MyDocData
{
    PMPageFormat             pageFormat;
    PMPrintSettings          printSettings;
}MyDocData;
```

See [Setting Up the Page Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummrt) for more information about this structure.

When the user chooses Print from the File menu, your application needs to do the following:

1. Create a printing session object.
2. Check for a valid page format object; if there isn’t one, create it.
3. Create a print settings object and set it to default values for this session. A print settings object (`PMPrintSettings`) is an opaque object that stores information such as the number of copies and range of pages. An application creates an instance of this object by calling the function `PMCreatePrintSettings`. Apple recommends that you do not save the print settings object with the document, as it is intended to describe print settings for a specific printing session.
4. Call the function `PMSessionUseSheets` to indicate that the Print dialog should use sheets. Although sheets are not available in Mac OS 9 and earlier, you should call this function if your application runs in Mac OS X as well as Mac OS 9. In Mac OS 9, the function returns a result code that indicates sheets are not available.
5. Call the Carbon Printing Manager function `PMSessionPrintDialog` to display the Print dialog so the user can specify settings such as page range and number of copies before printing. In Mac OS X, the dialog is displayed as a sheet as long as you called the function `PMSessionUseSheets`.
6. Release the printing session object, set the print settings object to `NULL`, and handle errors, if any occur. Apple recommends that your application does not save print settings from one session to the next, which is why you need to set the print settings object to `NULL`.

The function `MyDoPrint` in [Listing 3-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummrr) shows how your application can respond to the Print command. Following this listing is a detailed explanation for each line of code that has a numbered comment.

__Listing 2-6__  A function that responds to the Print command


```swift
OSStatus MyDoPrint (WindowRef documentWindow,
                            MyDocData *docDataP)// 1
{
    OSStatus status = noErr;// 2
    PMPrintSettings printSettings = NULL;
    PMPageFormat pageFormat = NULL;
    UInt32 minPage = 1, maxPage;
    PMPrintSession printSession;

    status = PMCreateSession (&printSession);// 3
    if (status == noErr)
     {
        status = MySetupPageFormatForPrinting (printSession,
                                        docDataP, &pageFormat);// 4
        if (status == noErr)
        {
            status = PMCreatePrintSettings (&printSettings);// 5
            if (status == noErr)
            {
                status = PMSessionDefaultPrintSettings (printSession,
                                        printSettings);// 6
                if (status == noErr)
                {
                    CFStringRef windowTitleRef;
                    status = CopyWindowTitleAsCFString (documentWindow,
                                    &windowTitleRef);// 7
                    if (status == noErr)
                    {
                        status = PMSetJobNameCFString (printSettings,
                                                    windowTitleRef);// 8
                        CFRelease (windowTitleRef);// 9
                    }
                }
            }
            if (status == noErr)
            {
                maxPage = MyGetDocumentNumPagesInDoc (docDataP);// 10
                status = PMSetPageRange (printSettings, // 11
                                            minPage, maxPage);
            }
            if (status == noErr)
            {
                 Boolean accepted;
                 Boolean sheetsAreAvailable = true;// 12
                 docDataP->printSettings = printSettings;// 13
                 status = PMSessionUseSheets (printSession,
                                            documentWindow,
                                            gMyPrintDialogDoneProc);// 14

                if (status == kPMNotImplemented)// 15
                {
                    status = noErr;
                    sheetsAreAvailable = false;
                }
                if (status == noErr)
                {
                    status = PMSessionPrintDialog (printSession,
                                                printSettings,
                                                pageFormat,
                                                &accepted);// 16
                     if (status == noErr && !sheetsAreAvailable)// 17
                                    MyPrintDialogDoneProc (printSession,
                                                parentWindow, accepted);
                }
            }
        }
        if (status != noErr)// 18
         {
            if (printSettings)
             {
                docDataP->printSettings = NULL;// 19
                (void) PMRelease (printSettings);
            }
            (void) PMRelease (printSession);    // 20
         }
    }
    MyPostPrintingError (status, kMyPrintErrorFormatStrKey);// 21
    return status;
}
```

Here’s what the code in [Listing 3-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummrr) does:

1. Passes a reference to the document window and a pointer to the data structure that contains the page format and print settings structures for the document. Your application can get the pointer (`docDataP`) to pass to your `MyDoPrint` function by calling the Window Manager function `GetWindowProperty`. This assumes that you have already set up the data structure and set it as a property of the window using the Window Manager function `SetWindowProperty`.
2. Sets up the local variables you need for this function. You need to declare local variable to hold print settings and page format objects and set them to `NULL`. You need two variables—`minPage` and `maxPage`—for getting and setting the page range. You need to declare a variable to hold a printing session object.
3. Calls the Carbon Printing Manager function `PMCreateSession` to create a printing session object.
4. Calls your application’s function to set up a page format object. See [Setting Up a Page Format Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywueqkki5bucskc). Pass the printing session, the pointer to the structure `MyDocData`, and a pointer to storage for the local page format object.
5. Calls the Carbon Printing Manager function `PMCreatePrintSettings` to allocate a local print settings object.
6. Sets default values for the print settings object for the current printing session.
7. Calls the Window Manager function `CopyWindowTitleAsCFString`. This example uses the document’s window title as the name of the print job.
8. Calls the Carbon Printing Manager function `PMSetJobNameCFString` to set the name of the print job.
9. Makes sure you call the Core Foundation Base Services function `CFRelease` to release the `CFStringRef` you created for the document’s window title.
10. Calls your application’s function to determine the number of pages in the document. See [Calculating the Maximum Number of Pages to Print](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummjt).
11. Calls the Carbon Printing Manager function `PMSetPageRange` to specify the actual range of pages in the document. In Mac OS X, the minimum allowable page (`minPage`) appears in the From field in the Copies & Pages pane of the Print dialog and the maximum allowable page (`maxPage`) appears in the To field. If the user enters a value outside of this range in the Print dialog the Carbon Printing Manager displays an alert message. The page range cannot be enforced automatically in Mac OS 8 and 9.
12. Sheets are not available in Mac OS 8 and 9. If you plan to run your application in Mac OS 8 and 9 as well as in Mac OS X, you need to write your code so it acts properly in both situations. This code demonstrates how you can support each operating system. First, create a variable `sheetsAreAvailable` and set it to `true`.
13. Writes the print settings object to the document’s data structure to allow the object to be accessed by your application’s Print dialog done function.
14. Calls the Carbon Printing Manager function `PMSessionUseSheets` to specify that a printing dialog (in this case the Print dialog) should be displayed as a sheet.

    You need to pass the current printing session, the window that contains the document to be printed, and a pointer to your Print dialog done function. The Carbon Printing Manager calls your Print dialog done function when the user dismisses the Print dialog. This code assumes the application already declared a global variable:

```
gMyPrintDoneProc = NewPMSheetDoneUPP (MyPrintDoneProc);
```

    If your application runs in Mac OS 8 or 9, calling the function `PMSessionUseSheets` returns the error `kPMNotImplemented`, and the function has no effect.
15. Checks for the error `kPMNotImplemented`. If it is returned, this means your application is running in Mac OS 8 or 9, and that you are responsible for calling your procedure to handle dismissal of the Print dialog. Set `sheetsAreAvailable` to `false`.
16. Calls the Carbon Printing Manager function `PMSessionPrintDialog`, to display the Print dialog. Pass the current printing session, the print settings and page format objects that were set up in previous steps, and a pointer to a Boolean value. You call this function regardless of the version of the operating system. If your application is running in Mac OS X, the dialog appears as a sheet.

    The following is true if you are using sheets:

    - When the user dismisses the Print dialog, the Carbon Printing Manager calls the function specified by `gMyPrintDialogDoneProc` in the previous call to `PMSessionUseSheets.`
    - When using sheets, the `PMSessionPrintDialog` function returns immediately and the Boolean value returned in the `accepted` variable is irrelevant since it is your Print dialog done function that is called when the dialog is dismissed. If your application needs to perform additional tasks after the user dismisses the Print dialog, it can do so in the `MyPrintDoneProc` function, which is called when the user dismisses the Print dialog.
    - If the user clicks the OK button in the Print dialog, the print settings object is updated with the user’s changes (if any) and the value `true` is returned to the `MyPrintDoneProc` function. If the user clicks the Cancel button, the print settings object is unchanged and the value `false` is returned to the `MyPrintDoneProc` function.

    The following is true if you are not using sheets:

    - The `PMSessionPrintDialog` function does not return until the user dismisses the Print dialog.
    - The Boolean value returned in the `accepted` variable is `true` if the user clicks OK and `false` if the user clicks Cancel.
17. If there is no error, and sheets are not available, then your application must call its Print dialog done function to handle dismissal of the Print dialog. See [Handling Dismissal of the Print Dialog](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummrq).
18. If an error is returned from the Print dialog, then you must release the printing session and print settings objects here. Otherwise you should release them in your Print dialog done function.
19. If there is an error, sets the print settings object stored in the document’s data structure to `NULL`.
20. If there is an error, releases the local printing session object.
21. Calls your application’s function to post a printing error. See [Handling Errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummju) for more information. If there is no error, the function does nothing.

There are a number of operations your application needs to do when the user dismisses the Print dialog. You should handle these in a Print dialog done function. This function is called by the Carbon Printing Manager if your application uses sheets. Otherwise, your application must call this function after it calls the function `PMSessionPrintDialog`.

The function `MyPrintDialogDoneProc` in [Listing 3-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummrs) shows how you can handle dismissal of the Print dialog in your application. It contains the minimum amount of code necessary to handle the dismissal, including calling the application’s print loop if the user accepts the Print dialog. If your application has more complicated printing needs, it may need to include code to perform other operations here. A detailed explanation for each line of code that has a numbered comment appears following the listing.

__Listing 2-7__  A function to handle dismissal of the Print dialog


```swift
static pascal void MyPrintDialogDoneProc (PMPrintSession printSession,
                                  WindowRef documentWindow,
                                 Boolean accepted)// 1
{
    OSStatus status = noErr, tempErr;
    MyDocData *docDataP = MyGetWindowProperty (documentWindow);// 2
    if (docDataP)
    {
        if (accepted)// 3
            status = MyDoPrintLoop (printSession,
                                    docDataP->pageFormat,
                                    docDataP->printSettings,
                                    docDataP);
        tempErr = PMRelease (ourDataP->printSettings);// 4
        if (status == noErr)
            status = tempErr;
         docDataP->printSettings = NULL;// 5
    }
    tempErr = PMRelease (printSession);// 6
    if (status == noErr)
        status = tempErr;
    MyPostPrintingError (status, kMyPrintErrorFormatStrKey);// 7
}
```

Here’s what the code in Listing 3-7 does:

1. The function takes three parameters: the current printing session object, a reference to document window, and a Boolean to indicate whether the user accepted or cancelled the Print dialog.
2. Calls your application’s function to retrieve a pointer to the structure `MyDocData`. If you set the pointer as a property of the document window using the Window Manager function `SetWindowProperty`, you can retrieve it using the Window Manager function `GetWindowProperty`. See the Window Manager documentation for more information.
3. If the user accepts the Print dialog (`accepted` has the value `true`), calls your application’s `MyDoPrintLoop` function to print the pages in the selected range. See [Writing the Print Loop](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummjq).
4. Calls the Carbon Printing Manager function `PMRelease` to release the print settings object. Releasing an object decrements its reference count, causing it to be deallocated when the count reaches 0. By not saving print settings between calls to the Print dialog, you ensure that the dialog displays with the appropriate default settings, which is the recommended behavior.
5. Sets the value of the print settings object to `NULL` to indicate it is no longer valid.
6. Calls the Carbon Printing Manager function `PMRelease` to release the printing session object.
7. Calls your application’s function to post a printing error. See [Handling Errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummju) for information on the error-posting function.

This section shows you how to write the code that actually creates a print job. Printing can occur only after valid page format and print settings objects are set up. In a document-based application, the printing code is typically called when the user clicks Print in the Print dialog. An application usually calls the printing code from its print dialog done procedure. See the call to the application-defined function `MyDoPrintLoop` from the function `MyPrintDialogDoneProc` (in [Handling Dismissal of the Print Dialog](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummrq)).

This section discusses the following tasks that your application needs to do to print a document:

- [Writing the Print Loop](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummjq)
- [Calculating the Maximum Number of Pages to Print](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummjt)
- [Drawing a Page](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummjs)

An application’s print loop code does most of its work by calling Carbon Printing Manager functions. The code loops over the page range specified by the user. Each pass through the loop, your application needs to call its page drawing function to draw one page. At each step through the print loop, your code should check for errors and take appropriate action if an error occurs.

The function `MyDoPrintLoop` in [Listing 3-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywueqkkjjdeessg) shows how your application can implement the print loop. You should be able to adapt this print loop code for applications with more sophisticated printing requirements. Following this listing is a detailed explanation for each line of code that has a numbered comment.

__Listing 2-8__  A function that implements a print loop


```
static OSStatus MyDoPrintLoop (PMPrintSession printSession,
                    PMPageFormat pageFormat,
                    PMPrintSettings printSettings,
                    const MyDocData *docDataP)// 1
{
    OSStatus err = noErr;// 2
    OSStatus tempErr = noErr;
    UInt32 firstPage, lastPage,
            totalDocPages = MyGetDocumentNumPagesInDoc (docDataP);// 3
    if (!err)
        err = PMGetFirstPage (printSettings, &firstPage);// 4
    if (!err)
                 err = PMGetLastPage (printSettings, &lastPage);// 5
    if (!err && lastPage > totalDocPages)// 6
             lastPage = totalDocPages;
    if (!err)
             err = PMSetLastPage (printSettings, lastPage, false);// 7
    if (!err)
        {
         err = PMSessionBeginDocument (printSession, printSettings,
                                pageFormat);// 8
        if (!err)
         {
            UInt32 pageNumber = firstPage;
             while (pageNumber <= lastPage && err == noErr &&
                            PMSessionError (printSession) == noErr)// 9
            {
                err = PMSessionBeginPage (printSession,
                                    pageFormat, NULL);// 10
                if (!err)
                 {
                    GrafPtr oldPort = NULL;
                    void *printingContext = NULL;
                    GetPort (&oldPort);// 11

                    err = PMSessionGetGraphicsContext (printSession,
                            kPMGraphicsContextQuickdraw,
                            (void **) &printingContext);// 12
                     if (!err)
                    {
                        Rect pageRect;
                        SetPort ((CGrafPtr) printingContext);// 13
                        GetPortBounds (printingContext, &pageRect);// 14
                        err = MyPageDrawProc (docDataP, &pageRect,
                                                 pageNumber)// 15
                        SetPort (oldPort);// 16
                    }
                    tempErr = PMSessionEndPage (printSession);// 17
                    if(!err)err = tempErr;
                }
                pageNumber++;// 18
             } // end while loop
            tempErr = PMSessionEndDocument (printSession);// 19
            if (!err)
                    err = tempErr;
            if (!err)
                    err = PMSessionError (printSession);// 20
            }
    }
    return err;
}
```

Here’s what the code in [Listing 3-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywueqkkjjdeessg) does:

1. The function takes four parameters: the current printing session object, a page format object, a print settings object, and pointer to the structure `MyDocData` (described in [Setting Up the Page Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummrt).
2. Declares two variable to keep track of error codes. This ensures an error that could occur in one part of the print loop won’t overwrite an error that occurs in another part.
3. Declares variables for the page numbers of the first and last pages to be printed and the number of pages that it is possible to print. Call your application’s function (`MyDetermineNumberOfPagesInDoc`) to figure out the maximum number of pages that can be printed. See [Calculating the Maximum Number of Pages to Print](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummjt) for more information.
4. Calls the Carbon Printing Manager function `PMGetFirstPage` to obtain the page number entered by the user in the From field in the Copies & Pages pane of the Print dialog. If the user does not enter a value, the function returns the value of the previous call to `PMSetFirstPage`, if any, or the default value.
5. Calls the Carbon Printing Manager function `PMGetLastPage` to obtain the page number entered by the user in the To field in the Copies & Pages pane of the Print dialog. If the user did not enter a value, the function returns the value of the previous call to `PMSetLastPage`, if any, or the default value.
6. If the user specified a last page number greater than the number of pages in the document, assigns the actual last page in the document to the variable `lastPage`.
7. Calls the Carbon Printing Manager function `PMSetLastPage` to set the last page of the page range in the print settings object for this print job. Setting the last page provides information used by the progress dialog that is shown during printing.
8. Calls the Carbon Printing Manager function `PMSessionBeginDocument` to establish a new print job.
9. Sets up a `while` loop over the range of pages selected for printing. Note that the loop terminates if any function returns an error (that is, if the variable `status` has a value other than `noErr`) or if the Carbon Printing Manager function `PMSessionError` returns an error.
10. Calls the Carbon Printing Manager function `PMSessionBeginPage` to inform the printing system that the drawing code which follows is part of a new page.
11. Calls the QuickDraw function `GetPort` to preserve the current graphics port.
12. Calls the Carbon Printing Manager function `PMSessionGetGraphicsContext` to obtain the QuickDraw graphics printing port for the page being printed.
13. Calls the QuickDraw function `SetPort` to set the graphics port to the port obtained in the previous step. You must do this before calling the document’s function to draw one page.
14. Calls the QuickDraw function `GetPortBounds` to get the page rectangle for the current printing context. Your application may prefer to use the functions `PMGetAdjustedPageRect` and `PMGetAdjustedPaperRect` for its drawing.
15. Calls your application’s function to draw the current page. See [Drawing a Page](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummjs) for more information.
16. Calls the `SetPort` function again to restore the port to the one you preserved previously.
17. Calls the Carbon Printing Manager function `PMSessionEndPage` to end the current page. You should use a temporary variable (`tempErr`) to get the status for this function so it doesn’t overwrite an existing, prior error. This approach ensures that the current page is always finished and that if any error occurs the loop terminates.
18. Increments the page count within the page-printing loop.
19. On completion of the page-printing loop, call the Carbon Printing Manager function `PMSessionEndDocument` to signal the completion of the print job.
20. Calls the Carbon Printing Manager function `PMSessionError` to determine if any printing error has occurred. If the user cancels the print job, the result code is `kPMCancel`.

The number of pages in a document is likely to depend on a number of factors, including document-specific changes by the user (such as adding text or changing font size), as well as Page Setup and Print dialog settings. Some applications might require a separate version of this function for each kind of document they print. Typically, you’d call the page calculation function from your print function (`MyDoPrint`). See [Listing 3-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummrr).

When you write your page calculation function, you should consider including code to do the following:

1. Call the Carbon Printing Manager function `PMGetAdjustedPaperRect` to obtain the paper size, taking into account orientation, application drawing resolution, and scaling settings. Applications can use this information to determine the number of pages in the document based on the current page format.

   If your application formats pages based on the page rectangle, you should instead call the Carbon Printing Manager function `PMGetAdjustedPageRect`.
2. Call the Carbon Printing Manager function `PMGetAdjustedPageRect` to obtain the page size (the imageable area), in points, taking into account orientation, application drawing resolution, and scaling settings.
3. Return the computed number of pages to print in the document.

The code you write to draw a page of a document needs to be tailored to support the specific needs of your application. You can call the Carbon Printing Manager function `PMGetAdjustedPageRect` to obtain the page size (the imageable area), in points, taking into account orientation, application drawing resolution, and scaling settings.

Regardless of how you implement page drawing, your application should check for errors after attempting to draw each page, and take the appropriate action should an error occur. Typically, you’d call your page drawing function from your print loop function. See [Listing 3-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywueqkkjjdeessg).

[Listing 3-9](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywueqkkizdeqqkc) shows a function that does some very simple text drawing.

__Listing 2-9__  A function that draws one page of a document


```
OSStatus MyPageDrawProc (const MyDocData *docDataP,
                            const Rect *drawingRectP,
                            UInt32 pageNumber)
{
    #pragma unused (docDataP, drawingRectP)
    OSStatus err = noErr;
    Str255 pageNumberString;

    MoveTo (72,72);
    TextFont (kFontIDHelvetica);
    TextSize (24);
    DrawString ("\pDrawing Page Number ");
    NumToString (pageNumber, pageNumberString);
    DrawString (pageNumberString);

    return err;
}
```


Handling errors is critical to providing printing support in any application. An application should handle any errors it gets, making sure it displays localized error strings to the user. Providing localized strings in Mac OS X is fairly easy if you define them in a separate file named `Localizable.strings` and follow the Mac OS X convention to put localized versions of the file into the appropriate language-specific folder.

You can create a `Localizable.strings` file in Project Builder by choosing New File from the File menu. Then, create an empty file named `Localizable.strings` and add it to the Resources group of your project. See _Inside Mac OS X: System Overview_ for detailed information on localizing strings, string file syntax, functions for retrieving strings, and information on generating a string file automatically.

[Listing 3-10](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummjqha) shows a function that displays an alert to notify the user that a printing error has occurred. The alert message includes a localized string and the error number. A detailed explanation for each line of code that has a numbered comment appears following the listing.

The function assumes a `Localizable.strings` file exists and contains a formatting string. A typical localized formatting string for a printing application would be:

```
"Print error format" = "There is an error in the printing code. Error number: %d.";
```

The string `"Print error format"` is the key. It is the string you pass to the function in Listing 3-10 as the `errorFormatStringKey` parameter. The string `"There is an error in the printing code. Error number: %d."` is the localized formatting string; it uses printf-style formatting.

__Listing 2-10__  A function to post a printing error alert


```
void MyPostPrintingError (OSStatus status,
                            CFStringRef errorFormatStringKey)// 1
{
    CFStringRef formatStr = NULL,
                printErrorMsg = NULL;
    SInt16      alertItemHit = 0;
    Str255      stringBuf;

    if ((status != noErr) && (status != kPMCancel))           // 2
    {
        formatStr =  CFCopyLocalizedString (errorFormatStringKey, NULL);// 3
        if (formatStr != NULL)
        {
            printErrorMsg = CFStringCreateWithFormat(
                       NULL, NULL,
                       formatStr, status);// 4
            if (printErrorMsg != NULL)
            {
                if (CFStringGetPascalString (printErrorMsg,
                              stringBuf, sizeof (stringBuf),
                              GetApplicationTextEncoding()))// 5
                 {
                     StandardAlert(kAlertStopAlert, stringBuf,
                                       NULL, NULL, &alertItemHit);// 6
                 }
                CFRelease (printErrorMsg);                     // 7
            }
           CFRelease (formatStr);                             // 8
        }
    }
}
```

Here’s what the code in [Listing 3-10](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywviucykjcummjqha) does:

1. The function takes two parameters: a result code (`status`) and a string (`CFStringRef`) that specifies a key associated with the localized format string.
2. Checks whether the passed error should be displayed. Any error except `kPMCancel`, indicating the user cancelled printing, should be displayed.
3. Calls the Core Foundation Bundle Services macro `CFCopyLocalizedString` to search the default strings file (`Localizable.strings`) for a localized format string that indicates how the error should be formatted for display. You need to pass the key (`errorFormatStringKey`) for the localized string you wish to retrieve. The second parameter is optional—it is a comment (`CFStringRef`) to help translators by giving them context or other hints about how the string is used or how to translate it. If you don’t provide a comment, you should pass `NULL`.
4. If no error occurs, calls the Core Foundation String Services function `CFStringCreateWithFormat` to create a copy of the error string that includes the error number. The first parameter is a reference to an allocator to be used to create the `CFString` object. You can pass `NULL` to request the default allocator. The second parameter refers to an undocumented feature, so pass `NULL`. The third parameter is a reference to a `CFString` object that contains a string with printf-style specifiers. The remaining parameters are arguments for the printf-style string. In this case there is only one, a status code.
5. Calls the Core Foundation String Services function `CFStringGetPascalString` to get a copy of the string in a format that can display in a standard alert dialog.
6. Calls the Dialog Manager function `StandardAlert` to display the error message.
7. Calls the Core Foundation Base Services function `CFRelease` to release the string (`printErrorMsg`) created by the call to `CFCopyLocalizedString`.
8. Calls the function `CFRelease` to release the string (`formatStr`) created by the call to `CFStringCreateWithFormat`.

This section provides information on what you need to do in your code to implement a command to save a document as a PDF file. In Mac OS X saving a document as a PDF file is simple. Your application needs to set the printing destination to a file location instead of to a printer. You set the destination by calling the function `PMSessionSetDestination`.

Listing 3-11 shows a code fragment that sets the destination to a PDF file. You need to supply the Carbon Printing Manager constants `kPMDestinationFile` to specify that the destination is a file and `kPMDocumentFormatPDF` that the document format is PDF. The parameter `saveURL` specifies the location to save the PDF file.

When you call the function `PMSessionSetDestination` you must

- call the function `PMSessionSetDestination` after a call to `PMCreateSession` and before you release the printing session object.
- use the same printing session object for the function `PMSessionSetDestination` as you use when you set defaults for the print settings object (`printSettings`).
- set the destination before you call your print loop code.

__Listing 2-11__  Setting the destination as a PDF file


```
if (status == noErr){
        status = PMSessionSetDestination (printSession,
                            printSettings,
                            kPMDestinationFile,
                            kPMDocumentFormatPDF,
                            saveURL);
 }
```

In addition to setting the destination as a PDF file, you need to decide how your application handles printing dialogs (Page Setup and Print) and whether you want the printing system to display the printing status dialog.

When users save a document, they expect to see a dialog in which they can specify a filename and file location. They do not expect to see Page Setup or Print dialogs. In most cases, your application should not display either of the printing dialogs to the user in response to the Save As PDF command. You need to write your printing code so that the print settings object is set up programmatically rather than by the user. Your application should use the current page format that is associated with the document.

The printing status dialog is automatically shown by the printing system when an application calls these functions: `PMSessionBeginDocument`, `PMSessionEndDocument`, `PMSessionBeginPage`, and `PMSessionEndPage`. The printing status message informs the user of the page being printed (Printing Page 1, Printing Page 2, and so forth). A printing status message is probably not appropriate to show for file saving so you should suppress the printing status dialog.

To suppress the printing status dialog, your application needs to use the “No Status Dialog” versions of these functions. Specifically, you call

- `PMSessionBeginDocumentNoDialog` instead of `PMSessionBeginDocument`
- `PMSessionEndDocumentNoDialog` instead of `PMSessionEndDocument`
- `PMSessionBeginPageNoDialog` instead of `PMSessionBeginPage`
- `PMSessionEndPageNoDialog` instead of `PMSessionEndPage`

Otherwise, the code you use to implement the print loop is the same as what you’d use to print a print job triggered by a user clicking Print in the Print dialog.

[Listing 3-12](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzyfvkfamzqgaydambugywueqkkinduir2k) shows a code fragment that assigns function names to an application-defined structure based on whether the status dialog should be shown. Then, the application passes a pointer to the structure to its print loop function (`MyDoPrintLoop`). You would need to modify your application’s print loop function to require a parameter that specifies a pointer to the application-defined structure containing the function names and call the appropriate function from the structure.

__Listing 2-12__  Setting up a print loop to use the No Dialog functions


```
 if (status == noErr)
 {
#if NO_STATUS_DIALOG
        PrintingProcs myPrintingProcs = {PMSessionBeginDocumentNoDialog,
                        PMSessionEndDocumentNoDialog,
                        PMSessionBeginPageNoDialog,
                        PMSessionEndPageNoDialog};
#else
        PrintingProcs myPrintingProcs = {PMSessionBeginDocument,
                        PMSessionEndDocument,
                        PMSessionBeginPage,
                        PMSessionEndPage};
#endif

                status = MyDoPrintLoop(printSession,
                            pageFormat,
                            printSettings,
                            documentDataP,
                            &myPrintingProcs);
 }
```


The Print One Copy command is often provided by applications as a shortcut to allow a user to print a single copy of a document using default settings. Because default print setting values are used, there is no need for your application to display the Print dialog. Instead your application should set up the print settings objects programmatically and should use the current page format that is associated with the document. Otherwise, the code you use to implement the print loop is the same as what you’d use to print a print job triggered by a user clicking Print in the Print dialog.

The Mac OS X printing system automatically handles printing multiple copies. Your application does not need to perform any tasks other than specifying the number of copies in the printing session object.

[Next](Adopting%20the%20Carbon%20Printing%20Manager.md)[Previous](Printing%20Concepts%20for%20Carbon%20Developers.md)

