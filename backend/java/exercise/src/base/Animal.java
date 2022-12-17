package base;

public abstract class Animals {
    private String name;

    public Animals(String name) {
        this.name = name;
    }

    public abstract void eat();
    public abstract void talk();
    public abstract void mating(Animals animal);

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
