import tests_general
import tests_home
import tests_field

def main():
    tests_general.run_all()
    tests_home.run_all()
    tests_field.run_all()
    print("All tests OK")

if __name__ == "__main__":
    main()
