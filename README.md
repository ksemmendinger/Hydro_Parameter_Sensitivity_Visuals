# A Visualization Workflow for Quantifying Parameter Sensitivities to Uncertainties for Hydrologic Models
## National Water Center Innovators Program: Summer Institute
### Hydroinformatics Theme
Authors: Kyla Semmendinger, Catherine Finkenbiner

### Project Overview and Workflow

![image](https://user-images.githubusercontent.com/20464090/61244868-d49ec100-a710-11e9-93b4-a123d959f169.png)

### Abstract
From regional to continental scales, models require modular components for representing individual hydrologic processes due to factors such as data availability and physical attributes. Therefore, the need for a common procedure within the hydrologic field to evaluate model output based on parameter sensitivities and uncertainties compared to performance metrics is evident. We developed a reproducible workflow for evaluating parameter sensitivities and uncertainties using the hydrologic modeling framework of the NOAA National Water Model (NWM). The NWM simulates observed and forecasted streamflow across the contiguous United States (CONUS) several times a day. High variability in soil types, elevations, vegetation characteristics, and forcings (e.g. precipitation) across CONUS leads to complexities when comparing model outputs and observed streamflow datasets. Our workflow objectively evaluates model output as a function of parameter choice using both numerical and visualization techniques. The workflow was implemented using case studies, provided by graduate student researchers at the National Water Center Innovators Program: Summer Institute. The results can be reproduced and visualized using python/R Jupyter notebooks within a community GitHub code repository. Model parameter sensitivity was evaluated using variance-based methods and Bayesian theory. Uncertainty in parameter spaces were quantified to highlight the impact of unreliable input data on model output. Model parameter sensitivities and uncertainties were evaluated numerically and visually to provide a comprehensive outlook on their impacts to model output. For each of the three case studies, we provided a summary and interpretation of the workflow results. Our workflow can be integrated into hydrologic modeling frameworks for objective modular model and parameter scheme evaluations based on a data-driven approach for model selection.

To clone this repository to your local computer:
```
 git clone https://github.com/ksemmendinger/SI_Hydroinformatics/
```
Required python3 libraries:
```
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```
Required R libraries:
```
add libraries
```

#### All datasets for the individual case studies are available upon request.
