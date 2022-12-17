package animals;

import base.Animal;

public class Cat extends Animal {
    public Cat(String name) {
        super(name);
    }

    @Override
    public void eat() {
        System.out.print(super.getName() +" eat fish!");
    }

    @Override
    public void talk() {
        System.out.print(super.getName() +" is meow meow");
    }

    @Override
    public void mating(Animal animal) {
        System.out.print(super.getName() + "is mating with " + animal.getName());
    }
}
