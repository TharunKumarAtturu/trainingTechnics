#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main () {
	char *token;
	char total_weather_report[150], city_name[20];
	int counter = 0;
	printf("Enter the city name: ");
	// fflush(char city_name);
	gets(city_name);
	printf("%s", city_name);
	int length_of_city_name = strlen(city_name);
	// for(int counter_length = 0; counter_length < length_of_city_name; counter_length++ ) {
	// 	if(counter_length == 0 || city_name[counter_length] == ' ' ) {
	// 		city_name[counter_length] = toupper(city_name[counter_length]);
	// 		// int n = atoi(city_name[counter_length]);

	// 	}
	// }
	sprintf(total_weather_report, "curl -o total_weather_report.txt -s \"https://api.openweathermap.org/data/2.5/find?q=%s&units=metric&appid=794466004f7baef6a081aeefce29c4fb\"", city_name);
	system(total_weather_report);
	FILE *fp_pointer;
	char weather_valve[800];
	fp_pointer = fopen("total_weather_report.txt", "r");
	if (fp_pointer == NULL) {

		perror("unable to acess the file!");
		exit(0);
	}
	else {

		while(fgets(weather_valve, sizeof(weather_valve), fp_pointer) > 0) {
			token = strtok(weather_valve, "{");
			while (token != NULL) { 
				counter = counter + 1;
				if(counter == 4) {
					token = strtok(token, ":");
					token = strtok(NULL, ":");
					token = strtok(token, ",");
					printf("Present temperature in %s: %s%cc.\n", city_name, token,248);
					// token
				}
				token = strtok(NULL, "{");

			} 
		}
	}
	return 0;
}
