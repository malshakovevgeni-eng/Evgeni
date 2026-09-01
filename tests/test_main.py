from evgeni.main import main


def test_main(capsys) -> None:
    main()
    captured = capsys.readouterr()
    assert captured.out == "Проект Evgeni работает!\n"
