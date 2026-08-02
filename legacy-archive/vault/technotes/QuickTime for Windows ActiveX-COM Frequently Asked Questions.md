---
title: QuickTime for Windows ActiveX/COM Frequently Asked Questions
apple_id: DTS10003913
resource_type: Technical Note
platform: macOS
topic: null
technology: QuickTime
published: '2006-05-02'
source_url: https://developer.apple.com/library/archive/technotes/tn2120/_index.html
archived_at: '2026-07-26T19:54:08.808585Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2120

# QuickTime for Windows ActiveX/COM Frequently Asked Questions

__Important:__ This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Provides answers to many frequently asked questions about the QuickTime ActiveX/COM control, covering topics such as exporting, grabbing movie frames, event notifications and others.

[Exporting a movie to another format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojrgmwugsbrfvke4vcbi4yq)[Exporting a movie to another format without displaying the export dialog](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojrgmwugsbrfvke4vcbi4za)[Performing a batch export operation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojrgmwugsbrfvke4vcbi4zq)[Export settings dialog hangs my machine?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojrgmwugsbrfvke4vcbi4yta)[Getting single image frames from a movie](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojrgmwugsbrfvke4vcbi4ytc)[Register for event notifications](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojrgmwugsbrfvke4vcbi4yti)[Getting movie annotations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojrgmwugsbrfvke4vcbi4yts)[Other References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojrgmwugsbrfvke4vcbi4zdg)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojrgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Exporting a movie to another format

Q: How do I export a movie to another format?

A: If you want to allow the user to configure everything for the export operation (exporter type, file, options: same as QuickTime Player export) then use the following:

__Listing 1__  User configured export - VB 6

```
Private Sub exportWithUserSettings(Control As QTControl)

    Dim qt As QTQuickTime
    Dim ex As QTExporter

    On Error GoTo DoError

    Set qt = Control.QuickTime
    If qt.Exporters.count = 0 Then qt.Exporters.Add
    Set ex = qt.Exporters(1)

    'Set exporter data source - could also be a track
    ex.SetDataSource Control.Movie

    'Display the export dialog
    ex.ShowExportDialog

    Exit Sub

DoError:
    If Err.Number = &H8004FF80 Then
    ' MacOS error -128: user clicked "cancel" button so ignore
    Else
    MsgBox "ERROR: " + Hex(Err.Number)
    End If

End Sub
```

__Listing 2__  User configured export - C#

```
using AxQTOControlLib;

private void exportWithUserSettings(AxQTControl Control)
{

    // Perform export with user configured
    // settings.

    try
    {
        QTQuickTime qt = Control.QuickTime;

        if (qt.Exporters.Count == 0) qt.Exporters.Add();

        QTExporter ex = qt.Exporters[1];

        // Set exporter data source - could also be a track
        ex.SetDataSource(Control.Movie);

        // Display the export dialog
        ex.ShowExportDialog();
    }
    catch(COMException ex)
    {
        // MacOS error -128: user clicked "cancel" button so ignore
        if (ex.ErrorCode != -2147156096 )
            MessageBox.Show("Error code: " + ex.ErrorCode.ToString("X"), "Export Error");
    }
    catch(Exception ex)
    {
        MessageBox.Show(ex.ToString(), "Export Error");
    }

}
```

[Back to Top](#)

## Exporting a movie to another format without displaying the export dialog

Q: How do I export a movie to another format without displaying the export dialog?

A: You first need to create an instance of the `QTExporter` object and then you need to configure it by setting its data source (movie or track) and exporter type (QuickTime Movie, AVI, 3G, MPEG-4, PNG, etc.) as well as the file you want to export to. Then call `BeginExport`.

Here's how it looks:

__Listing 3__  Exporting without displaying the export dialog - VB 6

```
Private Sub exportWithoutDialog(Control As QTControl)

    Dim qt As QTQuickTime
    Dim ex As QTExporter

    On Error GoTo DoError

    Set qt = Control.QuickTime
    If qt.Exporters.count = 0 Then qt.Exporters.Add
    Set ex = qt.Exporters(1)

    'Set exporter type: AVI, 3G, MPEG-4, PNG, etc.
    ex.TypeName = "QuickTime Movie"

    'Set selection to export (optional)
    ex.StartTime = 0      'Optional
    ex.EndTime = Control.Movie.Duration      'Optional

    'Set exporter data source - could also be a track
    ex.SetDataSource Control.Movie

    'Set name and path for exported file
    ex.DestinationFileName = "D:\Movies\Exported\exportMovie.mov"

    'Do the export
    ex.BeginExport

    Exit Sub

DoError:
    If Err.Number = &H8004FF80 Then
    ' MacOS error -128: user clicked "cancel" button so ignore
    Else
    MsgBox "ERROR: " + Hex(Err.Number)
    End If

End Sub
```

__Listing 4__  Exporting without displaying the export dialog - C#

```
using AxQTOControlLib;

private void exportWithoutDialog(AxQTControl Control)
{
    try
    {
        QTQuickTime qt = Control.QuickTime;

        if (qt.Exporters.Count == 0) qt.Exporters.Add();

        QTExporter ex = qt.Exporters[1];

        // Set exporter type: AVI, 3G, MPEG-4, PNG, etc.
        ex.TypeName = "QuickTime Movie";

        // Set selection to export (optional)
        ex.StartTime = 0; // Optional
        ex.EndTime = Control.Movie.Duration; // Optional

        // Set exporter data source - could also be a track
        ex.SetDataSource(Control.Movie);

        ex.DestinationFileName = @"C:\Movies\exported.mov";

        ex.ShowProgressDialog = true;
        Cursor.Current = Cursors.WaitCursor;
        ex.BeginExport();
        Cursor.Current = Cursors.Arrow;
    }
    catch(COMException ex)
    {
        // MacOS error -128: user clicked "cancel" button so ignore
        if (ex.ErrorCode != -2147156096 )
            MessageBox.Show("Error code: " + ex.ErrorCode.ToString("X"), "Export Error");
    }
    catch(Exception ex)
    {
        MessageBox.Show(ex.ToString(), "Export Error");
    }

}
```

[Back to Top](#)

## Performing a batch export operation

Q: How do I perform a "batch" export operation, re-using the same export settings over and over again (similar to what can be done using the `MovieExportSetSettingsFromAtomContainer` C-function)?

A: As described previously, you first need to create an instance of the `QTExporter` object and then configure it by setting its data source and exporter type as well as the file you want to export to. Next, call `ShowSettingsDialog` to display the export options dialog for the selected exporter type, and then call `BeginExport`. Once you have configured an exporter, you can change its data source and reuse it with other movies and/or tracks as many times as you like.

You can also persist exporter settings by getting and setting the XML property (a string).

Here are some samples that should help.

__Listing 5__  Batch export operation - VB 6

```
' Test for the existence of a specific directory
Function DirExists(path As String) As Boolean
    On Error Resume Next
    DirExists = (Dir$(path & "\nul") <> "")
End Function

' Test for the existence of a specific file
Function FileExists(filename As String) As Boolean
    On Error Resume Next
    FileExists = (Dir$(filename) <> "")
End Function

' Write out a string to a text file
Sub WriteTextFileContents(Text As String, filename As String, _
    Optional AppendMode As Boolean)
    Dim fnum As Integer, isOpen As Boolean
    On Error GoTo Error_Handler
    ' Get the next free file number.
    fnum = FreeFile()
    If AppendMode Then
         Open filename For Append As #fnum
     Else
         Open filename For Output As #fnum
     End If
     ' If execution flow gets here, the file has been opened correctly.
     isOpen = True
     ' Print to the file in one single operation.
     Print #fnum, Text
     ' Intentionally flow into the error handler to close the file.
Error_Handler:
    ' Raise the error (if any), but first close the file.
    If isOpen Then Close #fnum
    If Err Then Err.Raise Err.Number, , Err.Description
End Sub

' Read text file contents as a string
Function ReadTextFileContents(filename As String) As String
    Dim fnum As Integer, isOpen As Boolean
    On Error GoTo Error_Handler
    ' Get the next free file number.
    fnum = FreeFile()
    Open filename For Input As #fnum
    ' If execution flow got here, the file has been open without error.
    isOpen = True
    ' Read the entire contents in one single operation.
    ReadTextFileContents = Input(LOF(fnum), fnum)
    ' Intentionally flow into the error handler to close the file.
Error_Handler:
    ' Raise the error (if any), but first close the file.
    If isOpen Then Close #fnum
    If Err Then Err.Raise Err.Number, , Err.Description
End Function

' Perform an export operation with custom settings
' Also saves these export settings to a file which
' can be later be retrieved and used for additional
' exports
Private Sub exportWithCustomSettings(Control As QTControl)

    'Perform export with custom configured
    'settings.

    'To perform an export operation with custom
    'configured Settings you first need to create
    'an instance of the QTExporter object and then
    'you need to configure it by setting its data
    'source (movie or track) and exporter type
    '(QuickTime Movie, AVI, 3G, MPEG-4, PNG, etc.)
    'as well as the file you want to export to.

    'Then call ShowSettingsDialog to display the
    'export options dialog for the selected exporter
    'type, and finally call BeginExport.

    'Once you have configured an exporter, you can
    'change its data source and reuse it with other
    'movies and/or tracks as many times as you like.
    'You can also persist exporter settings by getting
    'and setting the XML property (a string).

    On Error GoTo ErrorHandler

    If Control.Movie Is Nothing Then Exit Sub

    Dim qt As QTQuickTime
    Dim ex As QTExporter

    Set qt = Control.QuickTime
    If qt.Exporters.Count = 0 Then
        qt.Exporters.Add
    End If
    Set ex = qt.Exporters(1)

    'Set exporter type: AVI, 3G, MPEG-4, PNG, etc.
    ex.TypeName = "QuickTime Movie"

    'Set selection to export (optional)
    ex.StartTime = 0      'Optional
    ex.EndTime = Control.Movie.Duration  'Optional

    'Set exporter data source - could also be a track
    ex.SetDataSource Control.Movie

    Dim exportFilePath As String
    exportFilePath = "C:\Movies\Exported.mov"

    'Set name and path for exported file
    'ex.DestinationFileName = "C:\Movies\Exported.mov"
    ex.DestinationFileName = exportFilePath

    'Display the settings dialog for the selected exporter type
    ex.ShowSettingsDialog

    'Now do the actual export
    ex.BeginExport

    Dim exportSettingsPath As String
    exportSettingsPath = App.path + "\\Settings"

    Dim exportSettingsFileName As String
    exportSettingsFileName = exportSettingsPath + "\\" + ex.TypeName + ".plist"

    'Save Exporter Settings
    If DirExists(exportSettingsPath) = False Then
        MkDir exportSettingsPath
    End If
    WriteTextFileContents ex.Settings.XML, exportSettingsFileName, False

    Exit Sub

ErrorHandler:
    If Err.Number = &H8004FF80 Then
        ' MacOS error -128: user clicked "cancel" button so ignore
    Else
        Beep
        Dim errStr As String
        errStr = "Failed with error #" & Hex(Err.Number) & ", " & Err.Description
        MsgBox errStr, vbCritical
    End If

End Sub

' Perform export opertation using saved export settings (file)
Private Sub exportAgainWithSavedSettings(Control As QTControl)

    If Control.Movie Is Nothing Then Exit Sub

    Dim qt As QTQuickTime
    Dim ex As QTExporter

    Set qt = Control.QuickTime
    If qt.Exporters.Count = 0 Then
        qt.Exporters.Add
    End If
    Set ex = qt.Exporters(1)

    'Set exporter type: AVI, 3G, MPEG-4, PNG, etc.
    ex.TypeName = "QuickTime Movie"

    'Set exporter data source - could also be a track
    ex.SetDataSource Control.Movie

    'Load previous exporter settings if possible
    Dim exportSettingsPath As String
    exportSettingsPath = App.path + "\\Settings"

    Dim exportSettingsFileName As String
    exportSettingsFileName = exportSettingsPath + "\\" + ex.TypeName + ".plist"

    If (FileExists(exportSettingsFileName) = True) Then
        Dim cf As New CFObject
        cf.XML = ReadTextFileContents(exportSettingsFileName)
        ex.Settings = cf
    Else
        ex.ShowSettingsDialog
    End If

    'Export Movie
    ex.DestinationFileName = "C:\Movies\Exported2.mov"
    ex.ShowProgressDialog = True
    ex.BeginExport

End Sub
```

__Listing 6__  Batch export operation - C#

```
 QTQuickTime qt = axQTControl1.QuickTime;
    if (qt.Exporters.Count == 0) qt.Exporters.Add();
    QTExporter ex = qt.Exporters[1];

    ex.TypeName = "3G";
    ex.SetDataSource(axQTControl1.Movie);

    String exporterSettingsPath = Application.StartupPath + "\\Settings";
    String exporterSettingsFileName = exporterSettingsPath + "\\" +
    ex.TypeName + ".plist";

    //Configure Exporter
    ex.ShowSettingsDialog();

    //Export movie
    ex.DestinationFileName = "C:\Movies\Exported.mov";
    ex.ShowProgressDialog = true;
    ex.BeginExport();

    //Save exporter settings
    if (!Directory.Exists(exporterSettingsPath))
        Directory.CreateDirectory(exporterSettingsPath);
    StreamWriter sw = File.CreateText(exporterSettingsFileName);
    sw.Write(ex.Settings.XML);
    sw.Close();

    Next time you can reload these settings from the settings file and reuse them again:

    .
    .
    .
    QTQuickTime qt = axQTControl1.QuickTime;
    if (qt.Exporters.Count == 0) qt.Exporters.Add();
    QTExporter ex = qt.Exporters[1];

    ex.TypeName = "3G";
    ex.SetDataSource(axQTControl1.Movie);

    // Load previous exporter settings if available
    String exporterSettingsPath = Application.StartupPath + "\\Settings";
    String exporterSettingsFileName = exporterSettingsPath + "\\" +
    ex.TypeName + ".plist";

    if (File.Exists(exporterSettingsFileName))
    {
        StreamReader sr = new StreamReader(exporterSettingsFileName);
        CFObject cf = new CFObject();
        cf.XML = sr.ReadToEnd();
        ex.Settings = cf;
        sr.Close();
    }
    else
        ex.ShowSettingsDialog();

    //Export movie
    ex.DestinationFileName = "C:\Movies\Exported.mov";
    ex.ShowProgressDialog = true;
    ex.BeginExport();
```

[Back to Top](#)

## Export settings dialog hangs my machine?

Q: When I call the `ShowSettingDialog` from my VB 6 application it seems to hang when the export settings dialog appears -- I can't adjust the values for the export options or do anything else. To regain control I have to force quit the application. Is there something I'm doing wrong?

A: If you compile the VB 6 application and run the executable \*outside\* of the VB 6 development environment this will not be a problem (use File->Make "MyApp.exe" to build the application for execution outside the development environment). This locked dialog issue only occurs in VB 6 "Run Mode".

[Back to Top](#)

## Getting single image frames from a movie

Q: Is there a way to get an image of a single frame from a movie?

A: One way is to use the `copyFrame(VARIANT Time)` method of `QTMovie` to put a grab of the specified frame for the specified movie time on the clipboard. Then you can easily use  `Clipboard`  class methods (or the Win32 clipboard functions) to get the image in a useable format.

Something like this:

__Listing 7__  Getting an image for a movie frame - VB 6

```
Private Sub copyFrame(Control As QTControl)

    If Control.movie Is Nothing Then Exit Sub

    Dim movie As QTMovie
    Set movie = Control.movie

    ' grab a frame in the middle of the movie
    movie.copyFrame ((movie.EndTime - movie.StartTime) / 2)

    If Clipboard.GetFormat(vbCFBitmap) Then
        '   Draw movie frame, etc.
    End If

End Sub
```

__Listing 8__  Getting an image for a movie frame - C#

```
using AxQTOControlLib;

private void myCopyFrame(AxQTControl Control)
{
    if (Control.Movie == null) return;

    QTMovie theMovie = Control.Movie;

    // grab frame from middle of movie
    theMovie.CopyFrame((theMovie.EndTime - theMovie.StartTime) / 2);

    // frame is now on the clipboard so let's get the data
    IDataObject data = Clipboard.GetDataObject();
    if (data != null)
    {
        // do what you want with data...
    }
}
```

[Back to Top](#)

## Register for event notifications

Q: How do I register for `QTEvent` notifications? For example, I'd like to receive the streaming status messages such as "Buffering..." and others.

A: You can register for `QTEvent` notifications on a number of the QuickTime objects, most commonly the `QTMovie`, `QTTrack` and `QTQuickTime` objects. For "Buffering..." type status string notifications you should register for `qtEventShowStatusStringRequest` notifications on the movie instance once it is loaded.

Here's how:

__Listing 9__  Registering for `QTEvent` Status String Notifications - VB 6

```
'status string listener
QTControl1.Movie.EventListeners.Add _
    QTOLibrary.QTEventClassesEnum.qtEventClassApplicationRequest, _
    QTOLibrary.QTEventIDsEnum.qtEventShowStatusStringRequest
```

__Listing 10__  Registering for `QTEvent` Status String Notifications - C#

```
// status string listener
axQTControl1.Movie.EventListeners.Add(
    QTEventClassesEnum.qtEventClassApplicationRequest,
    QTEventIDsEnum.qtEventShowStatusStringRequest, 0, null);
```

Then, in your `QTEvent` handler simply look for this notification ID:

__Listing 11__  A `QTEvent` handler function for status string notifications - VB 6

```
Private Sub QTControl1_QTEvent(ByVal EventClass As Long, ByVal EventID As Long,_
ByVal Phase As Long, ByVal EventObject As QTOLibrary.IQTEventObject, _
Cancel As Boolean)

'Code to handle various QuickTime Events

Select Case EventID

    'status strings
    Case QTEventIDsEnum.qtEventShowStatusStringRequest
        Dim msg As String
        msg = EventObject.GetParam _
        (QTEventObjectParametersEnum.qtEventParamStatusString).ToString()
        Debug.Print "qtEventShowStatusStringRequest : " & msg

End Select

End Sub
```

__Listing 12__  A `QTEvent` handler function for status string notifications - C#

```
private void axQTControl1_QTEvent(object sender,
                  AxQTOControlLib._IQTControlEvents_QTEventEvent e)
{
   switch (e.eventID)
   {
        case (int) QTEventIDsEnum.qtEventShowStatusStringRequest:

          string msg = e.eventObject.GetParam(
              QTEventObjectParametersEnum.qtEventParamStatusString).ToString();
          Console.WriteLine("qtEventShowStatusStringRequest : {0}", msg);
          break;
   }
}
```

Some other useful notifications include:

```
// QTEventClassesEnum, QTEventIDsEnum

qtEventClassStateChange, qtEventRateWillChange
qtEventClassStateChange, qtEventMovieDidEnd
qtEventClassTemporal, qtEventTimeWillChange
qtEventClassProgress, qtEventExportProgress
qtEventClassAudio, qtEventAudioVolumeDidChange
```

[Back to Top](#)

## Getting movie annotations

Q: I'd like to get movie annotation data (movie title, author, and so on) with the `GetUserData` method. However, when I pass one of the user data identifiers (`qtAnnotationFullName`, `qtAnnotationAuthor`, and so on) to this method I always receive an empty string as a return value. What am I doing wrong?

A: If you ask for an annotation that doesn't exist the `QTMovie` object will generate an exception.

__Note:__ An exception is thrown for annotations which do not exist so they may be differentiated from empty annotations.

You can explicitly configure the `ErrorHandling` property of the QuickTime Control to generate COM exceptions as follows:

```
AxQTControl1.ErrorHandling = QTErrorHandlingOptionsEnum.qtErrorHandlingRaiseException
```

When you ask for an annotation that doesn't exist you'll want to catch but ignore the exception. For example, here's a simple function written in VB 6 showing how to do this:

__Listing 13__  Catching exceptions when getting movie annotations - VB 6.

```
Function GetMovieAnnotation(ByRef mov As QTMovie, ByVal annotationID As Long) _
  As String

    On Error Resume Next

    Dim valStr As String

    valStr = ""
    valStr = mov.Annotation(annotationID)

    GetMovieAnnotation = valStr

End Function
```

Now you can easily get movie metadata by calling this function as shown here:

__Listing 14__  Getting movie metadata - VB 6

```
Dim fullName As String
fullName = ""
fullName = fullName + "Full Name: " + GetMovieAnnotation(QTControl1.Movie, _
    QTAnnotationsEnum.qtAnnotationFullName)
fullName = fullName + vbCrLf
```

Here's C# code which does a similar thing:

__Listing 15__  Getting movie metadata - C#

```
// Get movie annotation data and catch any errors
private string Get_MovieAnnotation(int inAnnoID, QTMovie inMovie)
{
    string annoStr = string.Empty;
    if (inMovie != null)
    {
        try
        {
            // get movie annotation
            annoStr = inMovie.get_Annotation(inAnnoID);
        }
        catch
        {
            // an error here means movie does not contain
            // the desired annotation
        }
    }
    return annoStr;
}

.
.
.
// Get Movie MetaData
    string fullName = string.Empty;
    QTMovie theMovie = axQTControl1.Movie;

    fullName = fullName + @"Full Name: " +
        Get_MovieAnnotation((int)QTAnnotationsEnum.qtAnnotationFullName, theMovie);
```

[Back to Top](#)

## Other References

- [MoviePlayer VB 6 sample code](https://developer.apple.com/samplecode/MoviePlayer/MoviePlayer.html)
- [MoviePlayer C# sample code](https://developer.apple.com/samplecode/MoviePlayerCSharp/MoviePlayerCSharp.html)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-05-02 | New document that provides answers to many frequently asked questions about the QuickTime ActiveX/COM control |

