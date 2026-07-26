---
title: 'Kreya 1.18 - What''s New | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/kreya-1.18-whats-new/'
original_language: en
published: 2025-09-26
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:84e82c1ec703c0b7'
translated: false
---

> 原文：[Kreya 1.18 - What's New | Kreya](https://kreya.app/blog/kreya-1.18-whats-new/)　·　Kreya Blog

Kreya 1.18 brings powerful new ways to visualize and validate your API workflows: **Data Previews** and **Snapshot Tests**. These features make it easier than ever to understand your API responses and ensure your integrations remain stable over time.

### Snapshot tests [Pro / Enterprise](https://kreya.app/pricing/)

Kreya 1.18 introduces **Snapshot Tests**, a fast, code-free way to ensure your APIs behave consistently over time. Inspired by Jest, snapshot tests automatically capture and compare API responses, alerting you to any unexpected changes.

**How snapshot tests work:**

- Enable snapshot testing in Kreya settings
- Kreya automatically saves a snapshot of each API response
- On future runs, responses are compared to the stored snapshot
- If the response changes, you’ll see a diff and can accept or reject the update

**Advanced usage:** For more control, use the `kreya.snapshot` API in your scripts to snapshot custom values:

```js
kreya.grpc.onResponse(async msg => await kreya.snapshot.verifyObjectAsJson('response', { length: msg.value.length }));
```

**Best practices:**

- Keep your tests deterministic, avoid random or time-dependent data in snapshots
- Treat snapshots like code: review changes, commit them to version control, and keep them up to date

![An animation showcasing snapshot testing.](https://kreya.app/whats-new/1.18/snapshot_testing.gif)

Test results are shown in the **Tests** tab, with visual snapshot diffs.  
 See the [snapshot documentation](https://kreya.app/docs/scripting-and-tests/tests/) for more details.

### Data Previews [Pro / Enterprise](https://kreya.app/pricing/)

Kreya now lets you create rich, interactive data visualizations directly in the app. With the new [`kreya.preview`](https://kreya.app/docs/scripting-and-tests/previews/) API, you can display PDFs, charts, HTML, and more, right from your scripts. This makes it easy to turn raw API responses into meaningful insights.

**Why use previews?**

- Visualize complex data for easier interpretation
- Share and review results with your team
- Debug and explore responses interactively

**Sample: Visualize API data as a chart**

You can render charts using libraries like Apache ECharts. For example, to visualize a REST API response as a bar chart:

```js
kreya.rest.onCallCompleted(  async resp =>    await kreya.preview.html(      `  <html>    <body>      <div id="chart" style="width: 100%; height: 100%;"></div>      <script src="https://cdn.jsdelivr.net/npm/[email protected]/dist/echarts.min.js"></script>      <script>        const chart = echarts.init(document.getElementById('chart'));        chart.setOption({            title: { text: 'Values' },            animation: false,            xAxis: { type: 'category', data: ${JSON.stringify(resp.response.content.map(d => d.label))} },            yAxis: { type: 'value' },            series: [{ type: 'bar', data: ${JSON.stringify(resp.response.content.map(d => d.value))} }]        });        window.addEventListener('resize', () => chart.resize());      </script>    </body>  </html>  `,      'Sales',    ),);
```

![An animation showcasing visualizing data as a chart.](https://kreya.app/whats-new/1.18/data_previews.gif)

See the [`kreya.preview` API documentation](https://kreya.app/docs/scripting-and-tests/general/kreya-base-script-api/#previewscriptapi) and [samples](https://kreya.app/docs/category/preview-data/) for more details and inspiration.

A small change, but sometimes really useful. It's now possible to store comments in environments.

![An animation showcasing add a comment in environments.](https://kreya.app/whats-new/1.18/environment_comments.gif)

### Improved trace and test tab

The Trace and Test tab has been redesigned. Messages are now grouped by operation name, making it quick and easy to see which message belongs to which operation. It is also now possible to search the Trace tab and navigate through the search results.

![An animation showcasing the improved test and trace tab.](https://kreya.app/whats-new/1.18/trace_and_test_tab.gif)

### Multiple organizations and seats manager in customer portal [Pro / Enterprise](https://kreya.app/pricing/)

There is now a dropdown menu in the header of the [customer portal](https://customers.kreya.app) for managing multiple organizations, whether personal or business. Additionally, the customer portal now features a new role called `Seats Manager`, which distinguishes between the billing administrator and the person responsible for managing user seats.

![Kreya customer portal screenshot](https://kreya.app/whats-new/1.18/membreco.png)

### GTK4 for Linux

On Linux, we updated our dependencies to GTK4. If you do not use Kreya via snap, make sure that you have `libgtk-4-1` and `libwebkitgtk-6.0-4` installed.

### Improved proxy support [Enterprise](https://kreya.app/pricing/)

It is now possible to configure proxy settings under `Project > Proxy`. Here, you can add a proxy address and exclusions. To activate a proxy, select it in the footer bar.

![An animation showcasing using the proxy settings.](https://kreya.app/whats-new/1.18/proxy.gif)

### And more

Kreya 1.18 also includes various improvements and bug fixes. For a full list, see the [release notes](https://kreya.app/docs/release-notes/).

If you have feedback or questions, please [contact us](https://kreya.app/cdn-cgi/l/email-protection#69010c05050629021b0c100847081919) or [report an issue](https://github.com/riok/Kreya/issues/new/choose).

Stay tuned! 🚀
