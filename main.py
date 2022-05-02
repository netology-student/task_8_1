
import superhero

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    info = superhero.SuperHeroInfo('2619421814940190')

    intelligence = {}
    intelligence['Hulk'] = info.get_intelligence('Hulk')
    intelligence['Captain America'] = info.get_intelligence('Captain America')
    intelligence['Thanos'] = info.get_intelligence('Thanos')

    print(intelligence)
    print(max(intelligence, key=intelligence.get))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
