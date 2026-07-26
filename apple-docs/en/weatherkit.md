---
title: WeatherKit
framework: WeatherKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/weatherkit
source_url: 'https://developer.apple.com/documentation/weatherkit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/weatherkit.json'
content_hash: 'sha256:061b44f8e1d1039b'
translated: false
---

> Navigation: [Technologies](technologies.md)

# WeatherKit

<sub>Framework</sub>

Deliver weather conditions and alerts to your users.

## Overview

WeatherKit provides timely weather information including current conditions, minute precipitation, along with hourly, and daily forecasts. It also provides severe weather alerts.

## Topics

### Fundamentals

- [Fetching weather forecasts with WeatherKit](weatherkit/fetching_weather_forecasts_with_weatherkit.md) — Request and display weather data for destination airports in a flight-planning app.
- [Weather](weatherkit/weather.md) — A model representing the aggregate weather data the caller requests.
- [WeatherService](weatherkit/weatherservice.md) — Provides an interface for obtaining weather data.

### Requests

- [WeatherQuery](weatherkit/weatherquery.md) — A structure that encapsulates a generic weather dataset request.
- [CurrentWeather](weatherkit/currentweather.md) — A structure that describes the current conditions observed at a location.
- [WeatherAttribution](weatherkit/weatherattribution.md) — A structure that  defines the necessary information for attributing a weather data provider.
- [WeatherMetadata](weatherkit/weathermetadata.md) — A structure that provides additional weather information.
- [WeatherSeverity](weatherkit/weatherseverity.md) — A description of the severity of the severe weather event.

### Characteristics

- [Precipitation](weatherkit/precipitation.md) — The form of precipitation.
- [PressureTrend](weatherkit/pressuretrend.md) — The atmospheric pressure change over time.
- [UVIndex](weatherkit/uvindex.md) — The expected intensity of ultraviolet radiation from the sun.
- [Wind](weatherkit/wind.md) — Contains wind data of speed, direction, and gust.
- [WeatherCondition](weatherkit/weathercondition.md) — A description of the current weather condition.

### Alerts and forecasts

- [WeatherAlert](weatherkit/weatheralert.md) — A weather alert issued for the requested  location by a governmental authority.
- [WeatherAvailability](weatherkit/weatheravailability.md) — A structure that indicates the availability of data at the requested location.
- [Forecast](weatherkit/forecast.md) — A forecast collection for minute, hourly, and daily forecasts.
- [MinuteWeather](weatherkit/minuteweather.md) — A structure that represents the next hour minute forecasts.
- [HourWeather](weatherkit/hourweather.md) — A structure that represents the weather conditions for the hour.
- [DayWeather](weatherkit/dayweather.md) — A structure that represents the weather conditions for the day.

### Celestial information

- [SunEvents](weatherkit/sunevents.md) — An enumeration that represents dates of solar events, including sunrise, sunset, dawn, and dusk.
- [MoonEvents](weatherkit/moonevents.md) — A structure that represents lunar events.
- [MoonPhase](weatherkit/moonphase.md) — An enumeration that specifies the moon phase kind.

### Errors

- [WeatherError](weatherkit/weathererror.md) — An error WeatherKit returns.

### Deprecations

- [Deprecated symbols](weatherkit/deprecations.md) — Review unsupported symbols and their replacements.

### Structures

- [CloudCoverByAltitude](weatherkit/cloudcoverbyaltitude.md) — Contains the percentage of sky covered by low, medium and high altitude cloud.
- [DailyWeatherStatistics](weatherkit/dailyweatherstatistics.md) — A structure that holds a collection of day weather statistics data.
- [DailyWeatherStatisticsQuery](weatherkit/dailyweatherstatisticsquery.md) — A structure that encapsulates a generic daily weather statistics dataset request.
- [DailyWeatherSummary](weatherkit/dailyweathersummary.md) — A structure that holds a collection of day weather summaries.
- [DailyWeatherSummaryQuery](weatherkit/dailyweathersummaryquery.md) — A structure that encapsulates a generic daily weather summary dataset request.
- [DayPartForecast](weatherkit/daypartforecast.md) — A structure that represents the weather forecast for part of the day.
- [DayPrecipitationStatistics](weatherkit/dayprecipitationstatistics.md) — A structure that describes precipitation statistics for a day.
- [DayPrecipitationSummary](weatherkit/dayprecipitationsummary.md) — A structure that describes the precipitation summary for a day.
- [DayTemperatureStatistics](weatherkit/daytemperaturestatistics.md) — A structure that describes temperature statistics for a day.
- [DayTemperatureSummary](weatherkit/daytemperaturesummary.md) — A structure that describes the temperature summary for a day.
- [HistoricalComparisons](weatherkit/historicalcomparisons.md) — A structure that represents the weather condition comparisons for a specific location. It’s a list of comparisons between current readings and historical averages. The list is ordered by significance of deviation.
- [HourTemperatureStatistics](weatherkit/hourtemperaturestatistics.md) — A structure that describes temperature statistics for a specific hour.
- [HourlyWeatherStatistics](weatherkit/hourlyweatherstatistics.md) — A structure that holds a collection of hour weather statistics data.
- [HourlyWeatherStatisticsQuery](weatherkit/hourlyweatherstatisticsquery.md) — A structure that encapsulates a generic hourly weather statistics dataset request.
- [MonthPrecipitationStatistics](weatherkit/monthprecipitationstatistics.md) — A structure that describes precipitation statistics for a specific month.
- [MonthTemperatureStatistics](weatherkit/monthtemperaturestatistics.md) — A structure that describes temperature statistics for a specific month.
- [MonthlyWeatherStatistics](weatherkit/monthlyweatherstatistics.md) — A structure that holds a collection of month weather statistics data.
- [MonthlyWeatherStatisticsQuery](weatherkit/monthlyweatherstatisticsquery.md) — A structure that encapsulates a generic monthly weather statistics dataset request.
- [Percentiles](weatherkit/percentiles.md) — A structure that describes probability distributions for a measurable weather condition.
- [PrecipitationAmountByType](weatherkit/precipitationamountbytype.md) — A structure that provides a breakdown of amounts of all forms of precipitation that is expected to occur over a period of time.
- [SnowfallAmount](weatherkit/snowfallamount.md) — A structure that describes the snowfall amount over a period of time.
- [Trend](weatherkit/trend.md) — A structure describing an observed pattern in the data for weather at a location for a specific condition.
- [TrendBaseline](weatherkit/trendbaseline.md) — A type encapsulating everything there is to know about what a trend baseline is.
- [WeatherChange](weatherkit/weatherchange.md) — A structure that informs how certain measurable weather aspects are expected to change relative to before.
- [WeatherChanges](weatherkit/weatherchanges.md) — A structure that represents the Weather Change forecast. It provides a qualitative assessment of whether upcoming weather is significantly different from prior conditions.

### Enumerations

- [Deviation](weatherkit/deviation.md) — Describes a comparison between two values in a trend.
- [HistoricalComparison](weatherkit/historicalcomparison.md) — An enum that represents a recognized comparison in the statistical analysis of a location’s historical weather data.
