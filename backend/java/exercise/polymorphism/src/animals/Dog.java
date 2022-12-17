package animals;

import base.Animal;

public class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }

    @Override
    public void eat() {
       System.out.println(super.getName() +" eat bone!");
    }

    @Override
    public void talk() {
        System.out.println(super.getName() +" is wow wow");
    }

    @Override
    public void mating(Animal animal) {
        System.out.println(super.getName() + "is mating with " + animal.getName());
    }
}
