import animals.Cat;
import animals.Dog;
import base.Animal;

public class Main {
    public static void main(String[] argV) {
        Animal[] animals = new Animal[]{new Cat("cat"),new Dog("dog")};

        for (Animal animal: animals) {
            System.out.println("this animal is :" + animal.getName());
            animal.talk();
        }
    }
}
