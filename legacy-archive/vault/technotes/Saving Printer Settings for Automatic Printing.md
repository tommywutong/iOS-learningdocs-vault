---
title: Saving Printer Settings for Automatic Printing
apple_id: DTS10004231
resource_type: Technical Note
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2007-03-29'
source_url: https://developer.apple.com/library/archive/technotes/tn2155/_index.html
archived_at: '2026-07-26T19:54:09.095741Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2155

# Saving Printer Settings for Automatic Printing

The Printer ID is a unique internal representation that specifies a particular print queue. It is possible for the user to create multiple print queues that use the same user visible name, however each queue will have a unique Printer ID. To reliably reference a particular print queue, and therefore a specific printer, it is necessary to always use a Printer ID. The `PMPrinter` data type neatly wraps up both concepts in a single package. This Technote describes how you can save and restore a `PMPrinter` in order to save a printer that the user has selected.

Typically you do not need to know the Printer ID to print. However in some limited situations it makes sense to save the selected printer and automatically use it when needed (for example to print receipts for a point-of-sale application). The Printer ID provides the necessary persistent reference, since you cannot save a `PMPrinter` to your preferences. So using a Printer ID you can save a reference to a print queue that is valid for the life of that print queue.

[Collecting Printing Information](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrtgewugsbrfvjukq2ujfhu4mi)[Choosing From Available Printers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrtgewugsbrfvjvkqstivbviskpjyyq)[Obtaining Print settings via the Print & Page Setup Dialogs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrtgewugsbrfvjvkqstivbviskpjyza)[Saving and Loading Print Settings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrtgewugsbrfvjvkqstivbviskpjyzq)[Validating a Printer ID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrtgewugsbrfvjukq2ujfhu4ni)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrtgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Collecting Printing Information

Depending on the expected workflow of your application, there are a number of ways that you may wish to approach obtaining the original `PMPrinter` that you use to print.

One method is to obtain a list of available printers, and ask the user to choose one. This is acceptable if print options mean little to the consumer of your application; simply printing is the goal. Choosing From Available Printers demonstrates this method.

The second method is to ask the user to select a printer and print settings using the standard Print & Page Setup dialog boxes. This allows the user to set other options, such as page size and layout, as well as select the printer itself. In this case, you may also wish to save all print settings in addition to the printer selection. Obtaining Print settings via the Print & Page Setup Dialogs demonstrates this method.

In either case, the entire point is to save and restore this printer selection from your preferences. This is demonstrated in Saving and Loading Print Settings.

### Choosing From Available Printers

You can obtain a list of available printers by calling `PMServerCreatePrinterList`. This call will return a `CFArray` of PMPrinters containing all the printers that it was able to discover. Listing 1 demonstrates how to turn the `CFArray` of PMPrinters into a `CFArray` of printer names to display to the user.

__Note:__ The list that is returned by `PMServerCreatePrinterList` may not be as complete as the list that is available when you add a printer via the Print & Fax preference pane. However printers that the user has already setup (manually or automatically) will always appear in this list.

__Listing 1__  Obtaining the list of available printers

```
OSStatus CreatePMPrintersAndPrinterNames( CFArrayRef *outPrinters, CFArrayRef *outPrinterNames ) {     *outPrinters = NULL;     *outPrinterNames = NULL;     // Obtain the list of PMPrinters     OSStatus err = PMServerCreatePrinterList( kPMServerLocal, outPrinters );     if( err == noErr )     {         CFIndex i, count = CFArrayGetCount( printers );         // Create another array to hold the printer names. You may use this to create a menu or list for         // the user to select a printer.         CFMutableArrayRef printerNames = CFArrayCreateMutable( NULL, count, kCFTypeArrayCallBacks );         if( printerNames )         {             for(i = 0; i < count; ++i)             {                 PMPrinter printer = (PMPrinter)CFArrayGetValueAtIndex( printers, i );                 CFStringRef name = PMPrinterGetName( printer );                 CFArrayAppendValue( printerNames, name );             }         }         *outPrinterNames = printerNames;     }     return err; }
```

### Obtaining Print settings via the Print & Page Setup Dialogs

More flexibility is available however if you allow the user to select a printer and print settings using the standard Print Dialog. By doing so you allow the user to customize all of the print settings for the print job and save these settings as a template for future print jobs. After the user prints for the first time you can simply save the print settings and use them again later. Listing 2 shows you how to display a Print Dialog and obtain the printer and print settings in order to reuse them again later.

__Listing 2__  Saving Printer information from a Print Dialog

```
OSStatus CreatePageFormat( PMPageFormat * outFormat ) {     PMPrintSession printSession;     OSStatus err;     Boolean accepted;      // In order to create the Page Format we're going to     // ask the user to setup that page format using Page Setup.     *outFormat = NULL;      err = PMCreateSession( &printSession );     if( !err )     {         // We could create a session, so create and default the page format.         err = PMCreatePageFormat( outFormat );         if( !err )             err = PMSessionDefaultPageFormat( printSession, *outFormat );          // Present the Page Setup dialog, if the user cancels or there         // is an error, we'll dispose of the created page format,         // return a NULL format, and whatever error may have been returned         // from PMSessionPageSetupDialog.         err = PMSessionPageSetupDialog( printSession, *outFormat, &accepted );         if( err || !accepted )         {             PMRelease( *outFormat );             *outFormat = NULL;         }           PMRelease( printSession );     }     return err; }  OSStatus CreatePrintSettings( PMPageFormat ioFormat, PMPrinter * outPrinter, PMPrintSettings * outSettings) {     PMPrintSession printSession;     OSStatus err;     Boolean accepted = false;      *outPrinter = NULL;     *outSettings = NULL;      // In order to create the Print Settings & select a printer we'll     // ask the user to create their settings using the Print dialog.     err = PMCreateSession( &printSession );     if( !err )     {         // Validate the Page Format against the current Printer, which may update         // that format.         err = PMSessionValidatePageFormat( printSession, ioFormat, kPMDontWantBoolean );          // Create and default the print settings         if( !err )             err = PMCreatePrintSettings( outSettings );         if( !err )             err = PMSessionDefaultPrintSettings( printSession, *outSettings );          // Present the Print dialog.         if( !err )             err = PMSessionPrintDialog( printSession, *outSettings, ioFormat, &accepted );         if( !err && accepted )         {             // If the user accepted, then we'll retain the printer selected             // so that it survives the scope of this session.             // If there is an error getting the printer, then it will             // remain NULL             err = PMSessionGetCurrentPrinter( printSession, outPrinter );             if( !err )                 PMRetain( *outPrinter );         }         else         {             // We got an error, or the user canceled the operation             // so we'll release our settings and NULL them out.             // The PMPrinter hasn't been set yet, so it will remain NULL.             PMRelease( *outSettings );             *outSettings = NULL;         }          PMRelease( printSession );     }     return err; }
```

### Saving and Loading Print Settings

The simplest way to save a reference to the printer that your user has selected previously is via CFPreferences. The Printer ID is returned via a `CFString` and all flattened printer data is returned via a CFDataRef, both of which are easily stored via CFPreferences. Listing 3 shows how to save these settings to your preferences and Listing 4 shows you how to recover the printer and print settings from your preferences.

__Warning:__ Because the user can easily change their printer configuration during runtime, your code should be prepared for the situation where the printer that you are using does not exist. In this case your code should ask the user to select a new printer. You can see one way of checking validity in Validating a Printer ID

__Listing 3__  Saving Print Settings to your Preferences

```
OSStatus SavePrintSettings( PMPrintSession inSession, PMPrintSettings inSettings, PMPageFormat inFormat ) {     CFStringRef printerID;     PMPrinter printer;     CFDataRef flatSettings, flatFormat;     OSStatus err, tempErr;      // We need the current printer from the print session before we can do anything else     // If we get an error retrieving it, then we will simply return that error and do nothing else     err = PMSessionGetCurrentPrinter( inSession, &printer );     if( err == noErr )     {         // If PMSessionGetCurrentPrinter returns successfully, then the printer is valid         // for as long as the session is valid, therefore we will assume that the printer name is valid.         printerID = PMPrinterGetID( printer );         CFPreferencesSetAppValue( kPrinterID, printerID, kCFPreferencesCurrentApplication );         CFRelease( printerID );          tempErr = PMFlattenPrintSettingsToCFData( inSettings, &flatSettings );         if( tempErr == noErr )         {             // If we can flatten the print settings, then save them to preferences             CFPreferencesSetAppValue( kPrintSettings, flatSettings, kCFPreferencesCurrentApplication );             CFRelease( flatSettings );         }         else         {             // If we cannot flatten print settings, then remove them from preferences             CFPreferencesSetAppValue( kPrintSettings, NULL, kCFPreferencesCurrentApplication );         }          tempErr = PMFlattenPageFormatToCFData( inFormat, &flatFormat );         if( tempErr == noErr )         {             // If we can flatten the the page format, then save them to preferences             // if we could not, then we can reuse them with another printer             CFPreferencesSetAppValue( kPageFormat, flatFormat, kCFPreferencesCurrentApplication );             CFRelease( flatFormat );         }     }      return err; }
```

__Listing 4__  Recovering Print Settings from your Preferences

```
void CopyPrintSettings( CFStringRef * outPrinterID, PMPrintSettings * outSettings, PMPageFormat * outFormat ) {     CFDataRef flatSettings, flatFormat;      *outPrinterID = CFPreferencesCopyAppValue( kPrinterID, kCFPreferencesCurrentApplication );     *outSettings = NULL;     *outFormat = NULL;      // load the printer ID via CFPreferences     if( *outPrinterID != NULL )     {         flatSettings = CFPreferencesCopyAppValue( kPrintSettings, kCFPreferencesCurrentApplication );         flatFormat = CFPreferencesCopyAppValue( kPageFormat, kCFPreferencesCurrentApplication );          // Ignoring errors unflattening, as if there is an error the corresponding setting         // will be NULL, indicating that it wasn't available.         if( flatSettings != NULL )         {             PMUnflattenPrintSettings( flatSettings, outSettings );             CFRelease( flatSettings );         }          if( flatFormat != NULL )         {             PMUnflattenPageFormatWithCFData( flatFormat, outFormat );             CFRelease( flatFormat );         }     } }
```

[Back to Top](#)

## Validating a Printer ID

Since the user is able to reconfigure their printing setup at anytime, even while your application is running, in order to provide a seamless experience, you will need to validate the printer that you plan to print with prior to every printing operation. In order to do this, you need to try to recreate the `PMPrinter` from the Printer ID. This is not necessary in normal circumstances, as the standard Print dialog box and the default settings will automatically choose the correct printer.

__Listing 5__  Checking the Printer ID is valid

```
// This function demonstrates one way to validate a printer. // A more sensible method of doing this would be to attempt // to create the printer, use it on success, and ask the // user to update their settings on failure. Boolean IsValidPrinter( CFStringRef inPrinterID ) {     PMPrinter printer = PMPrinterCreateFromPrinterID( inPrinterID );     Boolean valid = printer != NULL;     // It is safe to pass NULL to PMRelease, as we'd just get an error     // since we just want to make sure that a non-NULL printer gets     // released, we can safely ignore that error.     PMRelease( printer );     return valid; }
```

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-03-29 | New document that describes how you can save a a user selected Printer, Print Settings and Page Format to disk. |

