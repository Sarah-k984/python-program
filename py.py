class Animal:
    def __init__(self, name,species):
        self.name = name

    def make_sound(self):
        print(f"{self.name} makes a sound.")
        def info(self):
            print(f"{self.name} is a {self.species}.")
            class cat(Animal):
                def __init__(self, name, breed,color):
                    super().__init__(name, species="cat")
                    self.breed = breed
                    self.color = color
                def make_sound(self):
                    print(f"{self.name} meows.")
                    def purr(self):
                        print(f"{self.name} purring.")
                        my_cat = cat("Whiskers", "Siamese", "white")
                        my_cat.info()
                        my_cat.make_sound()
                        my_cat.purr()
                        class bird(Animal):
                            def make_sound(self):
                                return super().make_sound() + " chirps."
                            def fly(self):  
                                print(f"{self.name} is flying.")
                            my_bird = bird("Tweety", species="canary")                                          
                            my_bird.info()
                            my_bird.make_sound()
                            my_bird.fly()
                            class dog(Animal):
                                def __init__(self, name, breed,color):
                                    super().__init__(name, species="dog")
                                    self.breed = breed
                                    self.color = color
                                def make_sound(self):
                                    print(f"{self.name} barks.")
                                    def fetch(self):
                                        print(f"{self.name} is fetching the ball.")
                                        my_dog = dog("Buddy", "Golden Retriever", "golden")
                                        my_dog.info()
                                        my_dog.make_sound()
                                        my_dog.fetch()
                                        Animal=cat

