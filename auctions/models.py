from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=50)


    def __str__(self):
        return self.categoryName


class Bid(models.Model):
    bid = models.IntegerField()
    user= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="userBid")

 


class Listing(models.Model):
    title = models.CharField(max_length=26)
    description = models.CharField(max_length=350)
    imageUrl = models.CharField(max_length=600)
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, blank=True, null=True, related_name="bidPrice")
    activeStatus = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="listing_watchlist")


    def __str__(self):
        return self.title 


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="userComment")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="listingComment")
    message = models.CharField(max_length=235)

    def __str__(self):
        return f"{self.author} comment on {self.listing}"


