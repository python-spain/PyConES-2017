# Generated by Django 2.2.2 on 2019-11-09 11:07

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [("proposals", "0006_auto_20191109_0024")]

    operations = [
        migrations.RemoveField(model_name="proposal", name="abstract_en_markup_type"),
        migrations.RemoveField(model_name="proposal", name="abstract_es_markup_type"),
        migrations.RemoveField(model_name="proposal", name="abstract_markup_type"),
        migrations.RemoveField(
            model_name="proposal", name="additional_notes_en_markup_type"
        ),
        migrations.RemoveField(
            model_name="proposal", name="additional_notes_es_markup_type"
        ),
        migrations.RemoveField(
            model_name="proposal", name="additional_notes_markup_type"
        ),
        migrations.AlterField(
            model_name="proposal",
            name="abstract",
            field=martor.models.MartorField(
                blank=True,
                default="",
                help_text="Resumen detallado. Se hará pública si la propuesta se acepta. Edita usando <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.",
                verbose_name="Resumen detallado",
            ),
        ),
        migrations.AlterField(
            model_name="proposal",
            name="abstract_en",
            field=martor.models.MartorField(
                blank=True,
                default="",
                help_text="Resumen detallado. Se hará pública si la propuesta se acepta. Edita usando <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.",
                null=True,
                verbose_name="Resumen detallado",
            ),
        ),
        migrations.AlterField(
            model_name="proposal",
            name="abstract_es",
            field=martor.models.MartorField(
                blank=True,
                default="",
                help_text="Resumen detallado. Se hará pública si la propuesta se acepta. Edita usando <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.",
                null=True,
                verbose_name="Resumen detallado",
            ),
        ),
        migrations.AlterField(
            model_name="proposal",
            name="additional_notes",
            field=martor.models.MartorField(
                blank=True,
                default="",
                help_text="Cualquier cosa que te gustaría hacer saber a los revisores para que la tengan en cuenta al ahora de hacer la selección. Esto no se hará público. Edita usando <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.",
                verbose_name="Notas adicionales",
            ),
        ),
        migrations.AlterField(
            model_name="proposal",
            name="additional_notes_en",
            field=martor.models.MartorField(
                blank=True,
                default="",
                help_text="Cualquier cosa que te gustaría hacer saber a los revisores para que la tengan en cuenta al ahora de hacer la selección. Esto no se hará público. Edita usando <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.",
                null=True,
                verbose_name="Notas adicionales",
            ),
        ),
        migrations.AlterField(
            model_name="proposal",
            name="additional_notes_es",
            field=martor.models.MartorField(
                blank=True,
                default="",
                help_text="Cualquier cosa que te gustaría hacer saber a los revisores para que la tengan en cuenta al ahora de hacer la selección. Esto no se hará público. Edita usando <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.",
                null=True,
                verbose_name="Notas adicionales",
            ),
        ),
    ]
