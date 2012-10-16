from django.contrib import admin

from .models import (PercentDiscount, 
        AbsoluteDiscount,
        CartItemPercentDiscount,
        CartItemAbsoluteDiscount
        )


class PercentDiscountAdmin(admin.ModelAdmin):
    pass

class AbsoluteDiscountAdmin(admin.ModelAdmin):
    pass


class CartItemPercentDiscountAdmin(admin.ModelAdmin):
    pass


class CartItemAbsoluteDiscountAdmin(admin.ModelAdmin):
    pass


admin.site.register(PercentDiscount, PercentDiscountAdmin)
admin.site.register(AbsoluteDiscount, AbsoluteDiscountAdmin)
admin.site.register(CartItemPercentDiscount, CartItemPercentDiscountAdmin)
admin.site.register(CartItemAbsoluteDiscount, CartItemAbsoluteDiscountAdmin)
