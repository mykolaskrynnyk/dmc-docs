---
name: DatesProvider
description: DatesProvider component lets you set various settings that are shared across all date components.
endpoint: /components/datesprovider
package: dash_mantine_components
category: Date Pickers
---

.. toc::


### CSS Extensions

.. admonition::CSS Extensions
   :icon: radix-icons:info-circled
   :color: red

   Date components require additional CSS styles.

The Date components require an additional CSS stylesheet.  See the [Getting Started](/getting-started) section for more information.

Be sure to include:
```python
app = Dash(external_stylesheets=[dmc.styles.DATES])
```
Or, if you want to include all optional stylesheets:
```python
app = Dash(external_stylesheets=dmc.styles.ALL)
```



### Usage

The DatesProvider component lets you set various settings that are shared across all date components. DatesProvider supports the following settings:

- `locale` – dayjs locale, note that you also need to import corresponding locale module from dayjs. Default value is en.
- `firstDayOfWeek` – number from 0 to 6, where 0 is Sunday and 6 is Saturday. Default value is 1 – Monday.
- `weekendDays` – an array of numbers from 0 to 6, where 0 is Sunday and 6 is Saturday. Default value is [0, 6] – Saturday and Sunday.

### Locale

DatePicker component uses [dayjs](https://day.js.org) behind the scenes. So you can easily customize locale by including
required locale data and setting the `locale`. Make sure to include proper localization file from dayjs library.

```python
from dash import Dash
import dash_mantine_components as dmc

scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/locale/ru.min.js",
]

app = Dash(__name__, external_scripts=scripts, external_stylesheets=[dmc.styles.DATES])
```

.. exec::docs.datesprovider.simple

### Keyword Arguments

#### DatesProvider

.. kwargs::DatesProvider
