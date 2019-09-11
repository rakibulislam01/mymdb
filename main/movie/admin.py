from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin

from .models import Movie, Person, Role, Vote, MovieImage


@register(Person)
class MaterialPersonAdmin(MaterialModelAdmin):
    list_display = ('first_name', 'last_name')
    icon_name = 'person'


@register(MovieImage)
class MaterialMovieImageAdmin(MaterialModelAdmin):
    icon_name = 'image'


@register(Vote)
class MaterialVoteAdmin(MaterialModelAdmin):
    icon_name = 'add'


@register(Role)
class MaterialRoleAdmin(MaterialModelAdmin):
    icon_name = 'personal_video'


@register(Movie)
class MaterialMovieAdmin(MaterialModelAdmin):
    icon_name = 'movie_filter'


# admin.site.register(Movie)
# admin.site.register(Person)
# admin.site.register(Role)
# admin.site.register(Vote)
# admin.site.register(MovieImage)

# Todo Django Material Administration
# Link: https://github.com/MaistrenkoAnton/django-material-admin
