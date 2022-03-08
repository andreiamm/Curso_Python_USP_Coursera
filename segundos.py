duracao = int(input("Por favor, entre com o número de segundos que deseja converter:"))

dias = duracao // 86400
restodia = duracao % 86400
horas = restodia // 3600
restohora = restodia % 3600
minutos = restohora // 60
segundos = restohora % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")
