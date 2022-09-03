# //------------ Parte 1 ------------//
# Punto 4
library(tidyverse)
library(nycflights13)
library(ggplot2)

# Punto 5
flights
length(flights) # Cantidad de columnas
nrow(flights) # Cantidad de filas
colnames(flights) # carrier -> aerolínea del vuelo


# //------------ Parte 2 ------------//
# Punto 6
unique(flights['carrier'])
unique(select(flights, 'carrier'))
unique(flights$'carrier')

# Punto 7
group_by_aerolinea <- group_by(flights, carrier)
mutate_n_vuelos <- mutate(group_by_aerolinea, n_vuelos=n())
filter_n_vuelos <- filter(mutate_n_vuelos, n_vuelos>1000)
df_final <- ungroup(filter_n_vuelos)

# Punto 8
unique(df_final$carrier) # Elijo DL, porque suena a Dark Lord
df_final_dl <- filter(df_final, carrier=='DL')

# Punto 9
ggplot(df_final_dl, aes(arr_delay)) +
  geom_histogram(bins = 200, fill = 'lightblue', colour = 'blue') +
  xlim(-80, 200)
ggplot(df_final_dl, aes(arr_delay)) + 
  geom_freqpoly(bins = 200, fill = 'lightblue', colour = 'blue') +
  xlim(-80, 200)
ggplot(df_final_dl, aes(arr_delay)) +
  geom_density(bins = 200, fill = c("#D55E00"), colour = c("#D55E00")) +
  xlim(-80, 200)

# Punto 10
# TODO: Ver como usar desvio e IQR
summ <- summarise(
  df_final_dl, 
  mean=mean(arr_delay, na.rm = TRUE), 
  mediana=median(arr_delay, na.rm = TRUE),
  sd=sd(arr_delay, na.rm = TRUE),
  IQR=IQR(arr_delay, na.rm = TRUE)
)
ggplot(df_final_dl, aes(arr_delay)) +
  geom_histogram(bins = 100, fill = 'blue', color = 'blue') +
  xlim(-80, 200) +
  labs(title='Histogram of flights 🛫', x="Delay", y="Count") +
  geom_vline(aes(xintercept = summ$mean, color="mean"), size=1.1) +
  geom_vline(aes(xintercept = summ$mediana, color="median"), size=1.1) +
  scale_color_manual(name="statistics", values=c(mean="red", median="green"))

# Punto 11
# JAJA