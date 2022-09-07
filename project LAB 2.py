# Name Yomsen Tsegaye
# lab 2

Age = float(input("Enter your age:"))
dog_age = Age * 7
dog_years = dog_age // 1

dog_months = ((dog_age % 1) * 12) //1
dog_days = (((((dog_age % 1) * 12)%1 )*30)//1)

print("Your age in dog years is", dog_years, "years", dog_months, "months", dog_days, "days")

cat_age = Age * 9
cat_years = cat_age // 1

cat_months = ((cat_age % 1) * 12) //1
cat_days = (((((cat_age % 1) * 12)%1 )*30)//1)


print("Your age in cat years is", cat_years, "years", cat_months, "months", cat_days, "days")

horse_age = ((((Age ** 2) - 47)/ 7) + 12) * 3
horse_years = horse_age // 1

horse_months = ((horse_age % 1) * 12) //1
horse_days = (((((horse_age % 1) * 12)%1 )*30)//1)

print("Your age in horse years is", horse_years, "years", horse_months, "months", horse_days, "days")
