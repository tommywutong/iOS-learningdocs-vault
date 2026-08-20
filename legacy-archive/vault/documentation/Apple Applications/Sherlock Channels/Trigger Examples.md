---
title: Sherlock Channels
apple_id: 10000121i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-04-09'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Sherlock/Tasks/TriggerExamples.html
archived_at: '2026-07-15T05:18:59.156700Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sherlock Channels](Introduction%20to%20Sherlock%20Channels.md)


[Next](Document%20Revision%20History.md)[Previous](Using%20Web%20Services.md)

# Trigger Examples

This article includes some sample triggers from the Yellow Pages channel that comes with Sherlock. These examples use a combination of JavaScript and XQuery code to perform searches for the user.

The following example shows some code from the Yellow Pages channel that handles URL-based search requests. If the user clicks a Sherlock link in an HTML browser, the browser sends the URL text to Sherlock for processing. By the time a URL reaches a specific trigger, Sherlock has parsed the URL text and determined which trigger to call.

In this example, the trigger responds to the path `URL.complete`, which Sherlock calls after it has parsed the URL attributes. The trigger expects the URL request to contain some other attributes and values, in this case a query string and either a `zip` attribute or a `city` and `state` attribute. It populates the data store with these values and then initiates the query. Because the same data store fields are used to store values entered into the controls of the channel’s interface by the user, the behavior is the same as if the user had entered the values and clicked the search button.

```
 <trigger language="JavaScript" path="URL.complete">
/* this trigger handles sherlock url query */
query = DataStore.Get("URL.query");
DataStore.Set("YellowPages.MainQueryField.objectValue", query);

zip = DataStore.Get("URL.zip");
if (zip)
{
    DataStore.Set("YellowPages.CityStateZipField.objectValue", zip);
}
else
{
    city = DataStore.Get("URL.city");
    state = DataStore.Get("URL.state");
    if (city != null &amp;&amp; state != null)
    {
        cityAndState = city + ", " + state;
        DataStore.Set("YellowPages.CityStateZipField.objectValue",
                cityAndState);
    }
}

DataStore.Notify("YellowPages.SearchButton.action");
</trigger>
```


The following example shows how the Yellow Pages channel responds to the user clicking the search button from the channel interface. The code for initiating a search from a URL click also calls this code to begin the search.

The following two triggers show the initial search setup. In the first trigger, clicking the button sends a new notification to perform the actual setup. The second trigger uses XQuery code to return a dictionary of paths and values. Upon return from the second trigger, Sherlock assigns each value to the path specified by its key, generating appropriate notifications for each assignment.

```
 <trigger language="JavaScript" path="YellowPages.SearchButton.action">
DataStore.Notify("YellowPages.action.yellowPagesSearchSetUp");
</trigger>

<trigger language="XQuery" path="YellowPages.action.yellowPagesSearchSetUp"
            notify="YellowPages.action.yellowPagesSearch">
dictionary(
    ("YellowPages.ResultsTable.dataValue", ()),
    ("YellowPages.ResultsTable.selectedRows", -1),
    ("YellowPages.NetworkArrows.animating", true())
)
</trigger>
```

Once the search parameters are set up, the final notification sent from the `yellowPagesSearchSetup` trigger is to the `YellowPages.action.yellowPagesSearch` path to perform the search. The trigger that responds to this path is shown in the following code listing. The `yellowPagesSearch` trigger performs the search using the web service `YellowPagesSearch` and puts a subset of the results in the channel’s results table. It then sets several other properties, storing old search data and keeping track of the current location in the search result set. The `yellowPagesSearchComplete` trigger performs some late housekeeping tasks to indicate to the user that the search is complete.

```
 <trigger language="XQuery" path="YellowPages.action.yellowPagesSearch"
            inputs="csz=YellowPages.CityStateZipField.objectValue,
            query=YellowPages.MainQueryField.objectValue,
            lastCsz=YellowPages.data.lastCityStateZip,
            lastQuery=YellowPages.data.lastQuery,
            moreString=YellowPages.clickAgainString,
            attemptNum=YellowPages.data.attemptNumber,
            lastResults=YellowPages.data.lastResults">
let $attemptNum := if (not($attemptNum)) then 0 else $attemptNum

let $newQuery := if (($query != $lastQuery) or ($csz != $lastCsz) or
            ($attemptNum = 0)) then 1 else 0
let $cityStateZip := string-replace($csz, "/", ", ")
let $resultsToSave := if ($newQuery) then YellowPagesSearch($cityStateZip,
            $query) else $lastResults

let $resultsCount := count($resultsToSave)
let $newResultsStart := 1+($attemptNum * 10)
let $resultsEndMax := $newResultsStart + 9
let $resultsEnd := if ($resultsCount &lt; $resultsEndMax) then $resultsCount
            else $resultsEndMax

let $resultsToShow := sublist($resultsToSave, 1, $resultsEnd)
let $moreResults := if ($resultsCount &gt; $resultsEnd) then 1 else 0
let $labelText := if ($moreResults) then $moreString else " "
let $attempt := if ($moreResults) then $attemptNum+1 else 0

return dictionary(
    ("YellowPages.ResultsTable.dataValue", $resultsToShow),
    ("YellowPages.data.lastResults", $resultsToSave),
    ("YellowPages.action.yellowPagesSearchComplete", unique-id()),
    ("YellowPages.ResultsTable.highlightedColumn", "distance"),
    ("YellowPages.ResultsTable.columns.distance.indicatorImage",
            "../shared/Ascending.tiff"),
    ("YellowPages.data.sortColumn", "distance"),
    ("YellowPages.data.sortOrder", "ascending"),
    ("YellowPages.ClickAgainText.stringValue", $labelText),
    ("YellowPages.data.lastCityStateZip", $csz),
    ("YellowPages.data.lastQuery", $query),
    ("YellowPages.data.attemptNumber", $attempt)
)
</trigger>

<trigger language="XQuery"
        path="YellowPages.action.yellowPagesSearchComplete">
dictionary(
    ("YellowPages.ResultsTable.selectedRows", 0),
    ("YellowPages.NetworkArrows.animating", false()) )
</trigger>
```


If your channel wants to redirect the user to another channel to handle some task, you can do so programmatically from your channel’s controls. To open another channel, simply ask Sherlock to open a URL that is prefaced with the sherlock web scheme identifier (`sherlock://`). When opening a channel, you can specify a URL with the location of the channel’s main XML file. For channels that are already registered with Sherlock, you can specify the channel identifier instead of a file URL. The following example opens a new Sherlock window for the Internet channel using the channel identifier. The example uses the `new_window` identifier to open the channel in a new window.

```
<trigger language=”JavaScript” path=”MyChannel.MyButton.action”>
    System.OpenURL(“sherlock://com.apple.internet?new_window”);
</trigger>
```

[Next](Document%20Revision%20History.md)[Previous](Using%20Web%20Services.md)

