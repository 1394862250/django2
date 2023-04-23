from django.contrib import admin

# Register your models here.


from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_time', 'approved')
    list_filter = ('approved', 'created_time', 'category', 'tags')
    search_fields = ('title', 'body', 'author')
    actions = ['approve_posts']
    exclude = ('comments',)

    def approve_posts(self, request, queryset):
        if request.user.has_perm('posts.approve_post'):
            if queryset.update(approved=True) == 1:
                message_bit = '通过了1篇新闻'
            else:
                message_bit = '通过了%s篇新闻' % queryset.count()
            self.message_user(request, '%s' % message_bit)
        else:
            self.message_user(request, '你没有权限通过新闻')

    approve_posts.short_description = '通过选中的新闻'

    def save_model(self, request, obj, form, change):
        if not request.user.has_perm('posts.approve_post'):
            obj.approved = False
        try:
            obj.author
        except AttributeError:
            obj.author = request.user
        if not request.user.has_perm('posts.change_author'):
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
