library(tidyverse)
library(nycflights13)
library(ggplot2)
library(ggridges)

flights

df_flights <- flights

colnames(flights)

group_by_aerolinea <- group_by(flights, carrier)
mutate_n_vuelos <- mutate(group_by_aerolinea, n_vuelos=n())
filter_n_vuelos <- filter(mutate_n_vuelos, n_vuelos>1000)
df_final_dl <- filter(filter_n_vuelos, carrier=='DL')
df_final_dl <- ungroup(filter_n_vuelos)

# Punto 1
df_month <- group_by(df_final_dl, month)

summ_tiempos <- summarise(
  df_month, 
  retrasos=sum(dep_delay, na.rm=TRUE),
  tiempo_ganado=sum(arr_delay-dep_delay, na.rm=TRUE)
)

# Punto 2
ggplot(data=summ_tiempos) +
  geom_bar(aes(x=factor(month), y=retrasos), width=0.5, stat='identity', fill="red")

# Punto 3
ggplot(data=summ_tiempos) +
  geom_bar(aes(x=factor(month), y=tiempo_ganado), width=0.5, stat='identity', fill="blue")

# Punto 4
ggplot(data=df_month) +
  geom_density_ridges(aes(x=dep_delay, y=factor(month), fill=factor(month)), quantile_lines=TRUE, alpha=0.7) +
  xlim(-50, 100) +
  labs(title="Retrasos de vuelos en carrier DL en cada mes", x="Retrasos", y="Meses")
