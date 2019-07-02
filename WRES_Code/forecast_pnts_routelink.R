library(dataRetrieval)
library(data.table)
library(ggplot2)
library(foreach)
library(rwrfhydro)
library(lubridate)
library(latex2exp)

# Temp hardcoded input files
FORCAST_PTS_FILE = file.path("","Volumes", "Seagate Backup Plus Drive", "HydroInformatics", "20190701", "sipsey_wilderness_restart_run","frxst_pts_out.txt")
ROUTE_LINK = file.path("","Volumes", "Seagate Backup Plus Drive", "HydroInformatics", "20190701", "sipsey_wilderness_restart_run","DOMAIN", "Route_Link.nc")
#FOLDER = "/Volumes/Seagate Backup Plus Drive/HydroInformatics/20190701/sipsey_wilderness_restart_run"

#FORCAST_PTS_FILE = "frxst_pts_out.txt"
#ROUTE_LINK = "Route_Link.nc"

routeLink = ReadRouteLink(ROUTE_LINK)
forcast_pts = ReadFrxstPts(FORCAST_PTS_FILE)

# Extract NHDPlus link number from forcast pnts file
# Only one point supported at the moment
linkNo = trimws(forcast_pts$st_id[1])

# Get USGS gageID that matches link number in forcast
# points files from route link
gageID = routeLink[which(routeLink$link == linkNo), ]$site_no

# Delete routeLink -- just clutter at this point
rm(routeLink)

# Convert date cols to understandable R format
forcast_pts$dateTime <- ymd_hms(forcast_pts$timest)

# Note start and end date captured from forcast points files
# IF NOT REAL DATE OR USGS DATA DNE WILL CRASH
startDate = min(as_date(forcast_pts$dateTime))
endDate = max(as_date(forcast_pts$dateTime))

obsDF = readNWISuv(siteNumbers=gageID,
                   parameterCd="00060",
                   startDate=startDate,
                   endDate=endDate)

# Convert date cols to understandable R format
obsDF$dateTime <- ymd_hms(obsDF$dateTime)

# Create column of $\frac{m^3}{s}$
obsDF["q_cms"] <- obsDF$X_00060_00000 / 35.314666212661

# Add data to plot
plt <- ggplot(data = forcast_pts, aes(x=dateTime, y=q_cms)) + 
  geom_line(aes(color = 'NWM Simulated')) +
  geom_line(data = obsDF, aes(color='Observed')) +
  labs(title = "NWM Simulated vs Gauging Station",
       subtitle = paste("USGS",gageID),
       y=TeX("Q $(m^3/s)$"),
       x="Time",
       colour=" "
  )


plt